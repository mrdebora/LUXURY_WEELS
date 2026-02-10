import csv
import os
from io import StringIO

from datetime import date
from flask import Flask, render_template, redirect, url_for, request, flash
from flask import Response
from flask import make_response
from flask_login import LoginManager, login_user, login_required, logout_user, UserMixin, current_user
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

basedir = os.path.abspath(os.path.dirname(__file__))
db_dir = os.path.join(basedir, 'database')
os.makedirs(db_dir, exist_ok=True)
db_path = os.path.join(db_dir, 'luxury.db')

app = Flask(__name__)
app.config['SECRET_KEY'] = 'luxury-secret'
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{db_path}'
db = SQLAlchemy(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message = 'Por favor, faça login para acessar esta página.'
login_manager.login_message_category = 'warning'

# MODELOS
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(150), nullable=False)

class Vehicle(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    brand = db.Column(db.String(100), nullable=False)
    model = db.Column(db.String(100), nullable=False)
    category = db.Column(db.String(50))
    transmission = db.Column(db.String(20))
    vehicle_type = db.Column(db.String(20))  # Carro ou Moto
    daily_rate = db.Column(db.Float, nullable=False)
    people_capacity = db.Column(db.Integer)
    image_url = db.Column(db.String(200))
    last_revision = db.Column(db.String(20))
    next_revision = db.Column(db.String(20))
    last_inspection = db.Column(db.String(20))

class Reservation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer)
    vehicle_id = db.Column(db.Integer)
    start_date = db.Column(db.String(20))
    end_date = db.Column(db.String(20))
    total_price = db.Column(db.Float)
    payment_method = db.Column(db.String(50))  

@app.route("/editar_reserva/<int:reserva_id>", methods=["GET", "POST"])
@login_required
def editar_reserva(reserva_id):
    reserva = Reservation.query.get_or_404(reserva_id)

    if reserva.user_id != current_user.id:
        flash("Não tem permissão para editar esta reserva.", "danger")
        return redirect(url_for('my_reservations')) 

    if request.method == "POST":
        nova_data_inicio = request.form.get("start_date")
        nova_data_fim = request.form.get("end_date")

        if not nova_data_inicio or not nova_data_fim:
            flash("Por favor, preencha todas as datas.", "warning")
            return redirect(request.url)

        reserva.start_date = nova_data_inicio
        reserva.end_date = nova_data_fim

        db.session.commit()
        flash("Reserva atualizada com sucesso!", "success")
        return redirect(url_for("my_reservations")) 

    return render_template("editar_reserva.html", reserva=reserva)


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))



@app.route('/')
def home():
    return render_template('home.html')


@app.route('/export/reservations')
@login_required
def export_reservations():
    reservations = Reservation.query.filter_by(user_id=current_user.id).all()
    vehicle_map = {v.id: v for v in Vehicle.query.all()}

    si = StringIO()
    cw = csv.writer(si, delimiter=';', quoting=csv.QUOTE_MINIMAL)
    
    # Cabeçalho do relatório
    cw.writerow(['LUXURY WHEELS - RELATÓRIO DE RESERVAS'])
    cw.writerow([f'Usuário: {current_user.username}'])
    cw.writerow([f'Data de Exportação: {datetime.now().strftime("%d/%m/%Y %H:%M")}'])
    cw.writerow([])  # Linha vazia
    
    # Cabeçalho das colunas
    cw.writerow([
        'ID Reserva',
        'Marca',
        'Modelo',
        'Categoria',
        'Tipo',
        'Transmissão',
        'Data Início',
        'Data Fim',
        'Dias',
        'Valor/Dia (€)',
        'Método Pagamento',
        'Valor Total (€)'
    ])

    total_reservas = 0
    total_dias = 0
    total_gasto = 0.0

    for r in reservations:
        vehicle = vehicle_map.get(r.vehicle_id)
        if vehicle:
            # Calcular dias
            try:
                d1 = datetime.strptime(r.start_date, "%Y-%m-%d")
                d2 = datetime.strptime(r.end_date, "%Y-%m-%d")
                dias = (d2 - d1).days
            except:
                dias = 0
            
            # Formatar datas para padrão brasileiro
            try:
                data_inicio_fmt = datetime.strptime(r.start_date, "%Y-%m-%d").strftime("%d/%m/%Y")
                data_fim_fmt = datetime.strptime(r.end_date, "%Y-%m-%d").strftime("%d/%m/%Y")
            except:
                data_inicio_fmt = r.start_date
                data_fim_fmt = r.end_date
            
            cw.writerow([
                r.id,
                vehicle.brand,
                vehicle.model,
                vehicle.category or 'N/A',
                vehicle.vehicle_type,
                vehicle.transmission or 'N/A',
                data_inicio_fmt,
                data_fim_fmt,
                dias,
                f"{vehicle.daily_rate:.2f}".replace('.', ','),
                r.payment_method or 'N/A',
                f"{r.total_price:.2f}".replace('.', ',')
            ])
            
            total_reservas += 1
            total_dias += dias
            total_gasto += r.total_price

    # Linha vazia antes do resumo
    cw.writerow([])
    
    # Resumo final
    cw.writerow(['RESUMO'])
    cw.writerow(['Total de Reservas:', total_reservas])
    cw.writerow(['Total de Dias:', total_dias])
    cw.writerow(['Valor Total Gasto (€):', f"{total_gasto:.2f}".replace('.', ',')])
    cw.writerow(['Valor Médio por Reserva (€):', f"{total_gasto/total_reservas:.2f}".replace('.', ',') if total_reservas > 0 else '0,00'])

    # UTF-8 com BOM para compatibilidade com Excel
    output_content = '\ufeff' + si.getvalue()
    output = make_response(output_content)
    
    # Nome do arquivo com data e hora
    filename = f"reservas_luxury_wheels_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"
    output.headers["Content-Disposition"] = f"attachment; filename={filename}"
    output.headers["Content-type"] = "text/csv; charset=utf-8"
    return output



@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        user = User.query.filter_by(username=username).first()
        if user and check_password_hash(user.password, password):
            login_user(user)
            return redirect(url_for('search'))
        else:
            flash('Login inválido. Verifique seu usuário e senha.', 'danger')
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        
        # Verificar se o usuário já existe ANTES de criar
        existing_user = User.query.filter_by(username=username).first()
        if existing_user:
            flash("Nome de usuário já existe. Escolha outro.", "warning")
            return redirect(url_for('register'))
        
        # Criar novo usuário apenas se não existir
        hashed_pw = generate_password_hash(password, method='pbkdf2:sha256')
        new_user = User(username=username, password=hashed_pw)
        db.session.add(new_user)
        db.session.commit()
        
        flash("Conta criada com sucesso! Faça login para continuar.", "success")
        return redirect(url_for('login'))
    return render_template('register.html')


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('home'))


@app.route('/add_reservation', methods=['GET', 'POST'])
@login_required
def add_reservation():
    if request.method == 'POST':
        vehicle_id = int(request.form.get('vehicle_id'))
        start_date = request.form.get('start_date')
        end_date = request.form.get('end_date')

        vehicle = Vehicle.query.get(vehicle_id)
        if not vehicle:
            flash("Veículo não encontrado.", "danger")
            return redirect(url_for('add_reservation'))

        d1 = datetime.strptime(start_date, "%Y-%m-%d")
        d2 = datetime.strptime(end_date, "%Y-%m-%d")
        days = (d2 - d1).days
        total_price = vehicle.daily_rate * days

        reservation = Reservation(
            user_id=current_user.id,
            vehicle_id=vehicle_id,
            start_date=start_date,
            end_date=end_date,
            total_price=total_price
        )
        db.session.add(reservation)
        db.session.commit()
        return redirect(url_for('search'))

    vehicles = Vehicle.query.all()
    return render_template('add_reservation.html', vehicles=vehicles)


from datetime import datetime

@login_required
def esta_disponivel(veiculo):

    hoje = datetime.today().date()


    if veiculo.last_inspection:
        try:
            inspecao = datetime.strptime(veiculo.last_inspection, "%Y-%m-%d").date()
            if (hoje - inspecao).days > 365:
                return False
        except:
            return False

    if veiculo.next_revision:
        try:
            revisao = datetime.strptime(veiculo.next_revision, "%Y-%m-%d").date()
            if revisao < hoje:
                return False
        except:
            return False


    reservas = Reservation.query.filter_by(vehicle_id=veiculo.id).all()
    for r in reservas:
        try:
            inicio = datetime.strptime(r.start_date, "%Y-%m-%d").date()
            fim = datetime.strptime(r.end_date, "%Y-%m-%d").date()
            if inicio <= hoje <= fim:
                return False
        except:
            continue

    return True

@app.route('/search')
@login_required
def search():
    brand = request.args.get('brand', '')
    category = request.args.get('category', '')
    vehicle_type = request.args.get('vehicle_type', '')
    max_price = request.args.get('max_price', type=float)
    start_date = request.args.get('start_date')
    end_date = request.args.get('end_date')

    query = Vehicle.query

    if brand:
        query = query.filter(Vehicle.brand.ilike(f"%{brand}%"))
    if category:
        query = query.filter(Vehicle.category.ilike(f"%{category}%"))
    if vehicle_type:
        query = query.filter(Vehicle.vehicle_type == vehicle_type)
    if max_price:
        query = query.filter(Vehicle.daily_rate <= max_price)

    vehicles = query.all()

    if start_date and end_date:
        disponiveis = []
        for v in vehicles:
            conflitos = Reservation.query.filter(
                Reservation.vehicle_id == v.id,
                Reservation.end_date >= start_date,
                Reservation.start_date <= end_date
            ).first()
            if not conflitos:
                disponiveis.append(v)
        vehicles = disponiveis

    return render_template('search.html', vehicles=vehicles)


@app.route('/reserve', methods=['GET', 'POST'])
@login_required
def reserve():
    if request.method == 'GET':
        vehicle_id = request.args.get('vehicle_id', type=int)
        vehicle = Vehicle.query.get_or_404(vehicle_id)

        # Verificações
        hoje = datetime.now().date()
        if vehicle.next_revision:
            try:
                if datetime.strptime(vehicle.next_revision, "%Y-%m-%d").date() < hoje:
                    flash("Este veículo está com a revisão vencida. Reserva bloqueada.", "warning")
                    return redirect(url_for('search'))
            except ValueError:
                pass
        if vehicle.last_inspection:
            try:
                if datetime.strptime(vehicle.last_inspection, "%Y-%m-%d").date() < hoje:
                    flash("Este veículo está com a inspeção vencida. Reserva bloqueada.", "warning")
                    return redirect(url_for('search'))
            except ValueError:
                pass

        return render_template('reserve.html', vehicle=vehicle)

    vehicle_id = int(request.form.get('vehicle_id'))
    start_date = request.form.get('start_date')
    end_date = request.form.get('end_date')
    payment = request.form.get('payment')

  
    conflitos = Reservation.query.filter(
        Reservation.vehicle_id == vehicle_id,
        Reservation.end_date >= start_date,
        Reservation.start_date <= end_date
    ).all()

    if conflitos:
        flash("Este veículo já está reservado nas datas selecionadas. Escolha outras datas.", "warning")
        return redirect(url_for('search'))

    vehicle = Vehicle.query.get(vehicle_id)
    d1 = datetime.strptime(start_date, "%Y-%m-%d")
    d2 = datetime.strptime(end_date, "%Y-%m-%d")
    days = (d2 - d1).days
    total_price = vehicle.daily_rate * days

    reservation = Reservation(
        user_id=current_user.id,
        vehicle_id=vehicle_id,
        start_date=start_date,
        end_date=end_date,
        total_price=total_price,
        payment_method=payment
    )

    db.session.add(reservation)
    db.session.commit()
    flash("Reserva realizada com sucesso! Verifique em 'Minhas Reservas'.", "success")
    return redirect(url_for('my_reservations'))



@app.route('/my_reservations')
@login_required
def my_reservations():
    reservations = Reservation.query.filter_by(user_id=current_user.id).all()
    vehicle_map = {v.id: v for v in Vehicle.query.all()}

    total_reservas = len(reservations)
    total_gasto = sum(r.total_price for r in reservations)
    ultima_data = max((r.start_date for r in reservations), default=None)

    return render_template(
        'my_reservations.html',
        reservations=reservations,
        vehicles=vehicle_map,
        total_reservas=total_reservas,
        total_gasto=total_gasto,
        ultima_data=ultima_data
    )


@app.route('/cancel_reservation/<int:reservation_id>', methods=['POST'])
@login_required
def cancel_reservation(reservation_id):
    reservation = Reservation.query.get_or_404(reservation_id)
    if reservation.user_id != current_user.id:
        flash("Não autorizado. Esta reserva não pertence a você.", "danger")
        return redirect(url_for('my_reservations'))

    db.session.delete(reservation)
    db.session.commit()
    flash("Reserva cancelada com sucesso.", "success")
    return redirect(url_for('my_reservations'))

@app.route("/editar_veiculo/<int:vehicle_id>", methods=["GET", "POST"])
@login_required
def editar_veiculo(vehicle_id):
    vehicle = Vehicle.query.get_or_404(vehicle_id)


    if request.method == "POST":
        vehicle.brand = request.form.get("brand")
        vehicle.model = request.form.get("model")
        vehicle.category = request.form.get("category")
        vehicle.vehicle_type = request.form.get("vehicle_type")
        vehicle.transmission = request.form.get("transmission")
        vehicle.people_capacity = int(request.form.get("people_capacity") or 0)
        vehicle.daily_rate = float(request.form.get("daily_rate"))
        vehicle.image_url = request.form.get("image_url")
        vehicle.last_revision = request.form.get("last_revision")
        vehicle.next_revision = request.form.get("next_revision")
        vehicle.last_inspection = request.form.get("last_inspection")

        db.session.commit()
        flash("Veículo atualizado com sucesso!", "success")
        return redirect(url_for("search")) 

    return render_template("editar_veiculo.html", vehicle=vehicle)


if __name__ == '__main__':
    with app.app_context():
        db.create_all()

    app.run(debug=True)

