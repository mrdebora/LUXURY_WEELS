# 🚗 Luxury Wheels - Sistema de Aluguel de Veículos de Luxo

[![GitHub](https://img.shields.io/badge/GitHub-Repository-black.svg?logo=github)](https://github.com/mrdebora/LUXURY_WEELS)
![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Flask](https://img.shields.io/badge/Flask-3.0+-green.svg)
![Bootstrap](https://img.shields.io/badge/Bootstrap-5.3-purple.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

Sistema web moderno e elegante para gerenciamento de aluguel de veículos de luxo, desenvolvido com Flask e design premium.



## ✨ Características Principais

### 🎨 Interface Moderna
- Design responsivo e elegante com Bootstrap 5
- Animações suaves e efeitos interativos em CSS3 e JavaScript
- Gradiente animado na página inicial
- Cards 3D com efeitos hover
- Sistema de alertas categorizados com ícones
- Barra de progresso de scroll
- Efeitos de ripple nos botões

### 🔐 Sistema de Autenticação
- Registro de usuários com validação
- Login seguro com hash de senhas (PBKDF2-SHA256)
- Proteção de rotas com Flask-Login
- Mensagens de feedback contextualizadas

### 🚙 Gestão de Veículos
- Catálogo completo de veículos de luxo
- Filtros avançados de pesquisa:
  - Por marca
  - Por categoria (Sedan, SUV, Esportivo, etc)
  - Por tipo (Carro ou Moto)
  - Por valor máximo diário
  - Por disponibilidade em datas específicas
- Informações detalhadas:
  - Marca e modelo
  - Categoria e tipo
  - Transmissão
  - Capacidade de passageiros
  - Valor da diária
  - Imagem do veículo
  - Dados de manutenção e inspeção

### 📅 Sistema de Reservas
- Criação de reservas com validação de disponibilidade
- Cálculo automático de preços em tempo real (JavaScript)
- Validação de datas (impede datas passadas)
- Múltiplos métodos de pagamento:
  - Cartão de Crédito
  - PayPal
  - Multibanco
- Visualização de todas as reservas do usuário
- Edição de datas de reservas
- Cancelamento com confirmação
- Dashboard com estatísticas:
  - Total de reservas
  - Valor total gasto
  - Data da última reserva

### 📊 Exportação de Dados
- Exportação de reservas em formato CSV
- Relatório completo com:
  - Cabeçalho personalizado com nome de usuário e data
  - Detalhes de cada reserva (ID, veículo, datas, valores, pagamento)
  - Resumo estatístico (total de reservas, dias, gastos)
  - Formato europeu (vírgula decimal, ponto e vírgula separador)
  - UTF-8 com BOM para compatibilidade com Excel
  - Nome de arquivo com timestamp

### 🔧 Sistema de Manutenção
- Controle de revisões (última e próxima)
- Controle de inspeções
- Bloqueio automático de veículos com manutenção vencida
- Alertas visuais para usuários

## 🛠️ Tecnologias Utilizadas

### Backend
- **Python 3.8+**
- **Flask 3.0+** - Framework web
- **Flask-SQLAlchemy** - ORM para banco de dados
- **Flask-Login** - Gerenciamento de sessões
- **Werkzeug** - Segurança e hashing de senhas
- **SQLite** - Banco de dados

### Frontend
- **HTML5** - Estrutura semântica
- **CSS3** - Estilos customizados avançados
- **JavaScript ES6+** - Interatividade
- **Bootstrap 5.3** - Framework CSS responsivo
- **Bootstrap Icons** - Biblioteca de ícones

### Recursos CSS/JS
- Animações CSS3 (keyframes, transitions, transforms)
- Efeitos visuais avançados (glow, float, pulse, ripple)
- Scroll reveal animations
- Counter animations
- 3D card effects
- Form validation
- Smooth scrolling
- Progress bar

## 📋 Pré-requisitos

- Python 3.8 ou superior
- pip (gerenciador de pacotes Python)
- Navegador web moderno (Chrome, Firefox, Edge, Safari)

## 🚀 Instalação

### 1. Clone o repositório
```bash
git clone https://github.com/mrdebora/LUXURY_WEELS.git
cd LUXURY_WEELS
```

### 2. Crie um ambiente virtual (recomendado)
```bash
python -m venv venv

# Windows
venv\Scripts\activate

# Linux/Mac
source venv/bin/activate
```

### 3. Instale as dependências
```bash
pip install -r requirements.txt
```

### 4. Execute a aplicação
```bash
python app.py
```

### 5. Acesse no navegador
```
http://localhost:5000
```

## 📦 Dependências

```txt
Flask>=3.0.0
Flask-SQLAlchemy>=3.0.0
Flask-Login>=0.6.0
Werkzeug>=3.0.0
```

## 🗂️ Estrutura do Projeto

```
luxury_wheels/
│
├── app.py                  # Aplicação principal Flask
├── README.md              # Este arquivo
├── requirements.txt       # Dependências Python
│
├── static/                # Arquivos estáticos
│   ├── css/
│   │   └── style.css     # Estilos customizados (779 linhas)
│   ├── js/
│   │   └── main.js       # Scripts JavaScript (347 linhas)
│   └── img/
│       └── (imagens)
│
├── templates/             # Templates HTML (Jinja2)
│   ├── base.html         # Template base
│   ├── home.html         # Página inicial
│   ├── login.html        # Login
│   ├── register.html     # Registro
│   ├── search.html       # Pesquisa de veículos
│   ├── reserve.html      # Fazer reserva
│   ├── my_reservations.html  # Minhas reservas
│   ├── editar_reserva.html   # Editar reserva
│   └── editar_veiculo.html   # Editar veículo
│
└── database/             # Banco de dados SQLite
    └── luxury.db
```

## 🎯 Funcionalidades Detalhadas

### Sistema de Usuários
- **Registro**: Validação de usuário único, hash de senha seguro
- **Login**: Autenticação com mensagens de erro específicas
- **Logout**: Encerramento seguro de sessão
- **Proteção**: Todas as rotas principais protegidas com `@login_required`

### Pesquisa e Filtros
- **Busca por texto**: Marca e categoria com ILIKE (case-insensitive)
- **Filtros combinados**: Todos os filtros funcionam simultaneamente
- **Verificação de disponibilidade**: Conflito de datas detectado automaticamente
- **Apresentação visual**: Cards com imagens, badges de preço, informações completas

### Processo de Reserva
1. Usuário pesquisa veículos disponíveis
2. Seleciona veículo e visualiza detalhes
3. Escolhe datas (com validação em tempo real)
4. Vê cálculo automático de dias e valor total
5. Seleciona método de pagamento
6. Confirma reserva
7. Recebe feedback de sucesso e é redirecionado

### Gestão de Reservas
- **Visualização**: Dashboard com cards visuais de cada reserva
- **Estatísticas**: Contador animado, totalizadores
- **Edição**: Alteração de datas com validação
- **Cancelamento**: Confirmação via JavaScript antes de deletar
- **Exportação**: CSV profissional com todas as informações

## 🎨 Design e UX

### Paleta de Cores
```css
--primary-color: #2c3e50    /* Azul escuro */
--secondary-color: #3498db  /* Azul claro */
--accent-color: #e74c3c     /* Vermelho */
--success-color: #27ae60    /* Verde */
--warning-color: #f39c12    /* Laranja */
--gold-color: #f1c40f       /* Dourado */
```

### Tipografia
- Font family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif
- Font weights: 400 (normal), 600 (semibold), 700 (bold), 900 (black)

### Animações Principais
- **fadeInUp**: Entrada suave de baixo para cima (1s)
- **gradientShift**: Animação de gradiente (15s loop)
- **glow**: Efeito de brilho pulsante (2s loop)
- **floating**: Flutuação suave (3s loop)
- **pulse**: Pulsação/batimento (2s loop)
- **ripple**: Onda ao clicar (0.6s)
- **successPulse**: Confirmação visual (0.6s)

### Responsividade
- **Desktop** (>768px): Layout completo, múltiplas colunas
- **Tablet** (768px): Ajustes em grid e espaçamentos
- **Mobile** (<768px): Menu colapsável, coluna única, elementos redimensionados

## 🔒 Segurança

- ✅ Senhas hasheadas com PBKDF2-SHA256
- ✅ Proteção CSRF do Flask
- ✅ Validação de propriedade de recursos (usuário só edita suas reservas)
- ✅ SQL injection prevenido (SQLAlchemy ORM)
- ✅ Validações client-side e server-side
- ✅ Sessões seguras com Flask-Login

## 📊 Banco de Dados

### Modelo: User
```python
- id: Integer (PK)
- username: String(150) (Unique)
- password: String(150) (Hash)
```

### Modelo: Vehicle
```python
- id: Integer (PK)
- brand: String(100)
- model: String(100)
- category: String(50)
- transmission: String(20)
- vehicle_type: String(20)
- daily_rate: Float
- people_capacity: Integer
- image_url: String(200)
- last_revision: String(20)
- next_revision: String(20)
- last_inspection: String(20)
```

### Modelo: Reservation
```python
- id: Integer (PK)
- user_id: Integer
- vehicle_id: Integer
- start_date: String(20)
- end_date: String(20)
- total_price: Float
- payment_method: String(50)
```

## 🌐 Rotas da Aplicação

| Rota | Método | Autenticação | Descrição |
|------|--------|--------------|-----------|
| `/` | GET | Não | Página inicial |
| `/login` | GET, POST | Não | Login de usuário |
| `/register` | GET, POST | Não | Registro de usuário |
| `/logout` | GET | Sim | Logout |
| `/search` | GET | Sim | Pesquisa de veículos |
| `/reserve` | GET, POST | Sim | Fazer reserva |
| `/my_reservations` | GET | Sim | Ver minhas reservas |
| `/editar_reserva/<id>` | GET, POST | Sim | Editar reserva |
| `/cancel_reservation/<id>` | POST | Sim | Cancelar reserva |
| `/editar_veiculo/<id>` | GET, POST | Sim | Editar veículo |
| `/export/reservations` | GET | Sim | Exportar CSV |

## 🧪 Como Testar

### 1. Criar uma conta
- Acesse `/register`
- Escolha um username e senha
- Faça login

### 2. Adicionar veículos (via código ou banco)
```python
vehicle = Vehicle(
    brand='Mercedes',
    model='C-Class',
    category='Sedan',
    transmission='Automática',
    vehicle_type='Carro',
    daily_rate=150.00,
    people_capacity=5,
    image_url='https://exemplo.com/imagem.jpg'
)
db.session.add(vehicle)
db.session.commit()
```

### 3. Testar funcionalidades
- ✅ Pesquisar veículos com filtros
- ✅ Fazer uma reserva
- ✅ Ver estatísticas
- ✅ Editar reserva
- ✅ Exportar CSV
- ✅ Cancelar reserva

## 📱 Compatibilidade de Navegadores

| Navegador | Versão Mínima | Status |
|-----------|---------------|--------|
| Chrome | 90+ | ✅ Totalmente suportado |
| Firefox | 88+ | ✅ Totalmente suportado |
| Safari | 14+ | ✅ Totalmente suportado |
| Edge | 90+ | ✅ Totalmente suportado |
| Opera | 76+ | ✅ Totalmente suportado |

## 🐛 Solução de Problemas

### Erro: "Login inválido"
- Verifique se o usuário existe
- Confirme se a senha está correta
- Senhas são case-sensitive

### Erro: "Veículo já reservado"
- As datas escolhidas conflitam com reserva existente
- Escolha outras datas
- Verifique disponibilidade na pesquisa

### CSV não abre corretamente no Excel
- O arquivo usa UTF-8 com BOM
- Separador: ponto e vírgula (;)
- Decimal: vírgula (,)
- Tente "Importar Dados" no Excel se duplo clique não funcionar

## 🚀 Melhorias Futuras

- [ ] Sistema de avaliações de veículos
- [ ] Upload de imagens de veículos
- [ ] Integração com APIs de pagamento
- [ ] Sistema de notificações por email
- [ ] Painel administrativo completo
- [ ] Histórico de manutenções detalhado
- [ ] Sistema de descontos e promoções
- [ ] Geolocalização de retirada/devolução
- [ ] App mobile (React Native/Flutter)
- [ ] Relatórios e gráficos avançados

## 📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo LICENSE para mais detalhes.

## 👥 Contribuições

Contribuições são bem-vindas! Por favor:

1. Fork o projeto
2. Crie uma branch para sua feature (`git checkout -b feature/NovaFuncionalidade`)
3. Commit suas mudanças (`git commit -m 'Adiciona nova funcionalidade'`)
4. Push para a branch (`git push origin feature/NovaFuncionalidade`)
5. Abra um Pull Request

## 📞 Suporte

Para suporte ou dúvidas:
- 📧 Abra uma [issue no GitHub](https://github.com/mrdebora/LUXURY_WEELS/issues)
- 💬 Entre em contato através do repositório

## 🎓 Autores

**Desenvolvido por:** [@mrdebora](https://github.com/mrdebora)

Desenvolvido com ❤️ para gerenciamento premium de veículos de luxo.

---

**Luxury Wheels** - *Veículos de luxo ao seu alcance* 🚗✨
