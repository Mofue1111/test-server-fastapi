
from fastapi import FastAPI, Request
import uvicorn
from datetime import datetime
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
import random

app = FastAPI()

# Подключение статических файлов (для реального проекта нужно создать директорию static)
# app.mount("/static", StaticFiles(directory="static"), name="static")

def get_base_html(title: str, content: str):
    return f"""
    <!DOCTYPE html>
    <html lang="ru">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>{title} | XYZ Company</title>
        <link rel="preconnect" href="https://fonts.googleapis.com">
        <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
        <link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@400;600;700&family=Roboto:wght@300;400;500&display=swap" rel="stylesheet">
        <style>
            :root {{
                --primary: #2563eb;
                --primary-dark: #1d4ed8;
                --secondary: #f59e0b;
                --dark: #1e293b;
                --light: #f8fafc;
                --gray: #94a3b8;
                --success: #10b981;
            }}
            
            * {{
                margin: 0;
                padding: 0;
                box-sizing: border-box;
            }}
            
            body {{
                font-family: 'Roboto', sans-serif;
                line-height: 1.6;
                color: var(--dark);
                background-color: var(--light);
                min-height: 100vh;
                display: flex;
                flex-direction: column;
            }}
            
            header {{
                background: linear-gradient(135deg, var(--primary), var(--primary-dark));
                color: white;
                box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
                position: sticky;
                top: 0;
                z-index: 100;
            }}
            
            nav {{
                max-width: 1200px;
                margin: 0 auto;
                padding: 1rem 2rem;
            }}
            
            .nav-container {{
                display: flex;
                justify-content: space-between;
                align-items: center;
            }}
            
            .logo {{
                font-family: 'Montserrat', sans-serif;
                font-weight: 700;
                font-size: 1.5rem;
                color: white;
                text-decoration: none;
                display: flex;
                align-items: center;
                gap: 0.5rem;
            }}
            
            .logo-icon {{
                font-size: 2rem;
            }}
            
            .nav-links {{
                display: flex;
                gap: 1.5rem;
            }}
            
            .nav-links a {{
                color: white;
                text-decoration: none;
                font-weight: 500;
                font-family: 'Montserrat', sans-serif;
                padding: 0.5rem 1rem;
                border-radius: 0.5rem;
                transition: all 0.3s ease;
                position: relative;
            }}
            
            .nav-links a:hover {{
                background-color: rgba(255, 255, 255, 0.1);
            }}
            
            .nav-links a::after {{
                content: '';
                position: absolute;
                bottom: 0;
                left: 50%;
                width: 0;
                height: 2px;
                background-color: var(--secondary);
                transition: all 0.3s ease;
            }}
            
            .nav-links a:hover::after {{
                width: 100%;
                left: 0;
            }}
            
            main {{
                flex: 1;
                max-width: 1200px;
                margin: 2rem auto;
                padding: 0 2rem;
                width: 100%;
            }}
            
            .hero {{
                background: linear-gradient(rgba(0, 0, 0, 0.6), rgba(0, 0, 0, 0.6)), url('https://images.unsplash.com/photo-1450101499163-c8848c66ca85?ixlib=rb-4.0.3&auto=format&fit=crop&w=1350&q=80');
                background-size: cover;
                background-position: center;
                color: white;
                padding: 5rem 2rem;
                border-radius: 1rem;
                margin-bottom: 2rem;
                text-align: center;
                animation: fadeIn 1s ease-in-out;
            }}
            
            @keyframes fadeIn {{
                from {{ opacity: 0; transform: translateY(20px); }}
                to {{ opacity: 1; transform: translateY(0); }}
            }}
            
            h1 {{
                font-family: 'Montserrat', sans-serif;
                font-size: 2.5rem;
                margin-bottom: 1rem;
                color: var(--primary-dark);
            }}
            
            h2 {{
                font-family: 'Montserrat', sans-serif;
                font-size: 1.8rem;
                margin: 1.5rem 0 1rem;
                color: var(--primary);
            }}
            
            h3 {{
                font-family: 'Montserrat', sans-serif;
                font-size: 1.4rem;
                margin: 1.2rem 0 0.8rem;
            }}
            
            p {{
                margin-bottom: 1rem;
            }}
            
            .btn {{
                display: inline-block;
                background-color: var(--primary);
                color: white;
                padding: 0.7rem 1.5rem;
                border-radius: 0.5rem;
                text-decoration: none;
                font-weight: 500;
                transition: all 0.3s ease;
                border: none;
                cursor: pointer;
                font-family: 'Montserrat', sans-serif;
                margin: 0.5rem 0;
            }}
            
            .btn:hover {{
                background-color: var(--primary-dark);
                transform: translateY(-2px);
                box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
            }}
            
            .btn-secondary {{
                background-color: var(--secondary);
            }}
            
            .btn-secondary:hover {{
                background-color: #e69009;
            }}
            
            .card {{
                background-color: white;
                border-radius: 0.5rem;
                padding: 1.5rem;
                box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
                margin-bottom: 1.5rem;
                transition: transform 0.3s ease, box-shadow 0.3s ease;
            }}
            
            .card:hover {{
                transform: translateY(-5px);
                box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.1);
            }}
            
            .grid {{
                display: grid;
                grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
                gap: 1.5rem;
                margin: 2rem 0;
            }}
            
            .member {{
                text-align: center;
                padding: 1.5rem;
            }}
            
            .member img {{
                width: 150px;
                height: 150px;
                border-radius: 50%;
                object-fit: cover;
                margin-bottom: 1rem;
                border: 5px solid var(--primary);
            }}
            
            .contact-info {{
                background-color: white;
                padding: 2rem;
                border-radius: 0.5rem;
                box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
                margin: 2rem 0;
            }}
            
            .contact-info p {{
                margin-bottom: 0.8rem;
                display: flex;
                align-items: center;
                gap: 0.5rem;
            }}
            
            .contact-info i {{
                color: var(--primary);
                font-size: 1.2rem;
            }}
            
            footer {{
                background-color: var(--dark);
                color: white;
                text-align: center;
                padding: 2rem;
                margin-top: 2rem;
            }}
            
            .social-links {{
                display: flex;
                justify-content: center;
                gap: 1rem;
                margin: 1rem 0;
            }}
            
            .social-links a {{
                color: white;
                font-size: 1.5rem;
                transition: color 0.3s ease;
            }}
            
            .social-links a:hover {{
                color: var(--secondary);
            }}
            
            .branch-card {{
                position: relative;
                overflow: hidden;
                height: 300px;
                border-radius: 0.5rem;
            }}
            
            .branch-image {{
                width: 100%;
                height: 100%;
                object-fit: cover;
                transition: transform 0.5s ease;
            }}
            
            .branch-card:hover .branch-image {{
                transform: scale(1.1);
            }}
            
            .branch-overlay {{
                position: absolute;
                bottom: 0;
                left: 0;
                right: 0;
                background: linear-gradient(transparent, rgba(0, 0, 0, 0.8));
                padding: 1.5rem;
                color: white;
            }}
            
            .branch-overlay h3 {{
                color: white;
                margin-bottom: 0.5rem;
            }}
            
            .quick-links {{
                background-color: white;
                padding: 1.5rem;
                border-radius: 0.5rem;
                box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
                margin: 2rem 0;
            }}
            
            .quick-links h3 {{
                margin-bottom: 1rem;
                color: var(--primary);
            }}
            
            .quick-links ul {{
                list-style-type: none;
                display: flex;
                flex-wrap: wrap;
                gap: 1rem;
            }}
            
            .quick-links li {{
                background-color: var(--light);
                padding: 0.5rem 1rem;
                border-radius: 0.5rem;
                transition: all 0.3s ease;
            }}
            
            .quick-links li:hover {{
                background-color: var(--primary);
            }}
            
            .quick-links li:hover a {{
                color: white;
            }}
            
            .quick-links a {{
                color: var(--dark);
                text-decoration: none;
                font-weight: 500;
            }}
            
            @media (max-width: 768px) {{
                .nav-container {{
                    flex-direction: column;
                    gap: 1rem;
                }}
                
                .nav-links {{
                    flex-direction: column;
                    gap: 0.5rem;
                    width: 100%;
                }}
                
                .nav-links a {{
                    display: block;
                    text-align: center;
                }}
                
                .grid {{
                    grid-template-columns: 1fr;
                }}
            }}
        </style>
    </head>
    <body>
        <header>
            <nav>
                <div class="nav-container">
                    <a href="/" class="logo">
                        <span class="logo-icon">🏢</span>
                        <span>XYZ Company</span>
                    </a>
                    <div class="nav-links">
                        <a href="/">Главная</a>
                        <a href="/news">Новости</a>
                        <a href="/management">Руководство</a>
                        <a href="/about">О компании</a>
                        <a href="/branches">Филиалы</a>
                        <a href="/contacts">Контакты</a>
                    </div>
                </div>
            </nav>
        </header>
        <main>
            {content}
        </main>
        <footer>
            <div class="social-links">
                <a href="#" aria-label="Facebook">📘</a>
                <a href="#" aria-label="Twitter">🐦</a>
                <a href="#" aria-label="Instagram">📷</a>
                <a href="#" aria-label="LinkedIn">💼</a>
            </div>
            <p>© Компания XYZ, {datetime.now().year}. Все права защищены.</p>
        </footer>
    </body>
    </html>
    """

@app.get("/", response_class=HTMLResponse)
async def home():
    content = """
    <section class="hero">
        <h1 style="color: white;">Инновации для вашего бизнеса</h1>
        <p style="font-size: 1.2rem; max-width: 800px; margin: 0 auto 2rem;">Мы создаем передовые решения, которые помогают компаниям достигать новых высот в цифровую эпоху.</p>
        <div style="display: flex; gap: 1rem; justify-content: center;">
            <a href="/about" class="btn">О компании</a>
            <a href="/contacts" class="btn btn-secondary">Связаться с нами</a>
        </div>
    </section>
    
    <section>
        <h2>Наши преимущества</h2>
        <div class="grid">
            <div class="card">
                <h3>Опыт</h3>
                <p>Более 10 лет на рынке IT-решений для бизнеса. Мы знаем, как сделать ваш бизнес эффективнее.</p>
            </div>
            <div class="card">
                <h3>Инновации</h3>
                <p>Используем самые современные технологии, чтобы обеспечить конкурентное преимущество нашим клиентам.</p>
            </div>
            <div class="card">
                <h3>Глобальное присутствие</h3>
                <p>Филиалы в 5 странах мира позволяют нам работать с клиентами по всему земному шару.</p>
                <a href="/branches" class="btn" style="padding: 0.5rem 1rem; font-size: 0.9rem;">Наши филиалы</a>
            </div>
        </div>
    </section>
    
    <section class="quick-links">
        <h3>Быстрые ссылки</h3>
        <ul>
            <li><a href="/news">Последние новости</a></li>
            <li><a href="/branches/Paris">Наш филиал в Париже</a></li>
            <li><a href="/management">Команда руководителей</a></li>
            <li><a href="/contacts">Контактная информация</a></li>
        </ul>
    </section>
    """
    return HTMLResponse(content=get_base_html("Главная", content))

@app.get("/news", response_class=HTMLResponse)
@app.get("/news/{path:path}", response_class=HTMLResponse)
async def news():
    content = """
    <h1>Последние новости</h1>
    
    <div class="card">
        <h2>Запуск нового продукта X-Tech</h2>
        <p style="color: var(--gray); margin-bottom: 1.5rem;">15.10.2023</p>
        <p>Мы рады представить наш новый продукт X-Tech, который революционизирует подход к управлению бизнес-процессами. Решение уже получило положительные отзывы от первых клиентов.</p>
        <div style="display: flex; gap: 1rem; margin-top: 1rem;">
            <a href="/about" class="btn" style="padding: 0.5rem 1rem; font-size: 0.9rem;">Подробнее о компании</a>
            <a href="/contacts" class="btn btn-secondary" style="padding: 0.5rem 1rem; font-size: 0.9rem;">Запросить демо</a>
        </div>
    </div>
    
    <div class="card">
        <h2>Открытие нового офиса в Москве</h2>
        <p style="color: var(--gray); margin-bottom: 1.5rem;">01.09.2023</p>
        <p>Сообщаем об открытии нового офиса в Москве в бизнес-центре "Серебряный город". Современное пространство площадью 2000 кв.м. позволит нам расширить команду и принимать больше клиентов.</p>
        <a href="/branches" class="btn" style="padding: 0.5rem 1rem; font-size: 0.9rem;">Все филиалы</a>
    </div>
    
    <div class="quick-links">
        <h3>Другие разделы</h3>
        <ul>
            <li><a href="/management">Наше руководство</a></li>
            <li><a href="/about">История компании</a></li>
            <li><a href="/branches/London">Лондонский филиал</a></li>
        </ul>
    </div>
    """
    return HTMLResponse(content=get_base_html("Новости", content))

@app.get("/management", response_class=HTMLResponse)
@app.get("/management/{path:path}", response_class=HTMLResponse)
async def management():
    content = """
    <h1>Наша команда</h1>
    <p style="margin-bottom: 2rem;">Профессионалы с многолетним опытом работы в индустрии</p>
    
    <div class="grid">
        <div class="card member">
            <img src="https://randomuser.me/api/portraits/men/32.jpg" alt="Иванов Иван">
            <h3>Иванов Иван</h3>
            <p style="color: var(--primary); font-weight: 500;">Генеральный директор</p>
            <p>Основатель компании с более чем 15-летним опытом в IT и управлении бизнесом.</p>
            <a href="/contacts" class="btn" style="padding: 0.5rem 1rem; font-size: 0.9rem;">Связаться</a>
        </div>
        
        <div class="card member">
            <img src="https://randomuser.me/api/portraits/women/44.jpg" alt="Петрова Мария">
            <h3>Петрова Мария</h3>
            <p style="color: var(--primary); font-weight: 500;">Финансовый директор</p>
            <p>Специалист в области финансового менеджмента и стратегического планирования.</p>
            <a href="/about" class="btn" style="padding: 0.5rem 1rem; font-size: 0.9rem;">О компании</a>
        </div>
        
        <div class="card member">
            <img src="https://randomuser.me/api/portraits/men/75.jpg" alt="Сидоров Алексей">
            <h3>Сидоров Алексей</h3>
            <p style="color: var(--primary); font-weight: 500;">Технический директор</p>
            <p>Эксперт в области разработки программного обеспечения и управления IT-проектами.</p>
            <a href="/news" class="btn" style="padding: 0.5rem 1rem; font-size: 0.9rem;">Последние новости</a>
        </div>
    </div>
    
    <div class="quick-links">
        <h3>Смотрите также</h3>
        <ul>
            <li><a href="/news">Последние новости</a></li>
            <li><a href="/branches">Наши филиалы</a></li>
            <li><a href="/about">История компании</a></li>
        </ul>
    </div>
    """
    return HTMLResponse(content=get_base_html("Руководство", content))

@app.get("/about", response_class=HTMLResponse)
@app.get("/about/{path:path}", response_class=HTMLResponse)
async def about():
    content = """
    <h1>О компании</h1>
    
    <div class="card">
        <h2>Наша история</h2>
        <p>Компания XYZ была основана в 2010 году как небольшой стартап с командой из 5 человек. Сегодня мы - международная компания с офисами в 5 странах и штатом более 500 сотрудников.</p>
        <p>Наш путь начался с идеи создания простых и эффективных IT-решений для малого бизнеса. С годами мы расширили наш портфель продуктов и теперь предлагаем комплексные решения для предприятий любого масштаба.</p>
        <a href="/management" class="btn" style="padding: 0.5rem 1rem; font-size: 0.9rem;">Наша команда</a>
    </div>
    
    <div class="card">
        <h2>Наши ценности</h2>
        <div style="display: flex; flex-wrap: wrap; gap: 1rem; margin: 1rem 0;">
            <div style="flex: 1; min-width: 200px; background-color: #eff6ff; padding: 1rem; border-radius: 0.5rem;">
                <h3 style="color: var(--primary);">Инновации</h3>
                <p>Мы постоянно ищем новые подходы и технологии, чтобы оставаться лидерами рынка.</p>
            </div>
            <div style="flex: 1; min-width: 200px; background-color: #eff6ff; padding: 1rem; border-radius: 0.5rem;">
                <h3 style="color: var(--primary);">Качество</h3>
                <p>Наши продукты проходят многоуровневое тестирование перед выпуском.</p>
            </div>
            <div style="flex: 1; min-width: 200px; background-color: #eff6ff; padding: 1rem; border-radius: 0.5rem;">
                <h3 style="color: var(--primary);">Клиентоориентированность</h3>
                <p>Мы выстраиваем долгосрочные отношения с клиентами, основанные на доверии.</p>
            </div>
        </div>
    </div>
    
    <div class="quick-links">
        <h3>Полезные ссылки</h3>
        <ul>
            <li><a href="/branches/Paris">Наш филиал в Париже</a></li>
            <li><a href="/contacts">Контакты</a></li>
            <li><a href="/news">Новости компании</a></li>
        </ul>
    </div>
    """
    return HTMLResponse(content=get_base_html("О компании", content))

@app.get("/contacts", response_class=HTMLResponse)
@app.get("/contacts/{path:path}", response_class=HTMLResponse)
async def contacts():
    content = """
    <h1>Контакты</h1>
    
    <div class="contact-info">
        <h2>Головной офис</h2>
        <p><span style="font-size: 1.2rem;">🏢</span> <strong>Адрес:</strong> г. Москва, ул. Примерная, 123, БЦ "Высоцкий", 25 этаж</p>
        <p><span style="font-size: 1.2rem;">📞</span> <strong>Телефон:</strong> +7 (495) 123-45-67</p>
        <p><span style="font-size: 1.2rem;">✉️</span> <strong>Email:</strong> info@company.com</p>
        <p><span style="font-size: 1.2rem;">🕒</span> <strong>Часы работы:</strong> Пн-Пт: 9:00-18:00</p>
        
        <div style="margin-top: 2rem;">
            <h3>Отделы</h3>
            <div style="display: flex; flex-wrap: wrap; gap: 1rem; margin-top: 1rem;">
                <div style="flex: 1; min-width: 200px;">
                    <p><strong>Продажи:</strong></p>
                    <p>sales@company.com</p>
                    <p>+7 (495) 123-45-68</p>
                </div>
                <div style="flex: 1; min-width: 200px;">
                    <p><strong>Поддержка:</strong></p>
                    <p>support@company.com</p>
                    <p>+7 (495) 123-45-69</p>
                </div>
                <div style="flex: 1; min-width: 200px;">
                    <p><strong>Карьера:</strong></p>
                    <p>career@company.com</p>
                    <p>+7 (495) 123-45-70</p>
                </div>
            </div>
        </div>
    </div>
    
    <div class="quick-links">
        <h3>Наши филиалы</h3>
        <ul>
            <li><a href="/branches/London">Лондон</a></li>
            <li><a href="/branches/Paris">Париж</a></li>
            <li><a href="/branches/Berlin">Берлин</a></li>
        </ul>
    </div>
    
    <div class="card">
        <h2>Форма обратной связи</h2>
        <form style="display: grid; gap: 1rem; margin-top: 1rem;">
            <div>
                <label for="name" style="display: block; margin-bottom: 0.5rem; font-weight: 500;">Ваше имя</label>
                <input type="text" id="name" style="width: 100%; padding: 0.7rem; border: 1px solid var(--gray); border-radius: 0.5rem;">
            </div>
            <div>
                <label for="email" style="display: block; margin-bottom: 0.5rem; font-weight: 500;">Email</label>
                <input type="email" id="email" style="width: 100%; padding: 0.7rem; border: 1px solid var(--gray); border-radius: 0.5rem;">
            </div>
            <div>
                <label for="message" style="display: block; margin-bottom: 0.5rem; font-weight: 500;">Сообщение</label>
                <textarea id="message" rows="4" style="width: 100%; padding: 0.7rem; border: 1px solid var(--gray); border-radius: 0.5rem;"></textarea>
            </div>
            <button type="submit" class="btn" style="justify-self: start;">Отправить</button>
        </form>
    </div>
    """
    return HTMLResponse(content=get_base_html("Контакты", content))

@app.get("/branches", response_class=HTMLResponse)
async def branches_list():
    content = """
    <h1>Наши филиалы</h1>
    <p style="margin-bottom: 2rem;">Мы представлены в нескольких странах мира, чтобы быть ближе к нашим клиентам</p>
    
    <div class="grid">
        <div class="card branch-card">
            <img src="https://images.unsplash.com/photo-1513635269975-59663e0ac1ad?ixlib=rb-4.0.3&auto=format&fit=crop&w=1350&q=80" alt="Лондон" class="branch-image">
            <div class="branch-overlay">
                <h3>Лондон</h3>
                <p>Наш первый международный филиал</p>
                <a href="/branches/London" class="btn" style="padding: 0.5rem 1rem; font-size: 0.9rem; margin-top: 0.5rem;">Подробнее</a>
            </div>
        </div>
        
        <div class="card branch-card">
            <img src="https://images.unsplash.com/photo-1431274172761-fca41d930114?ixlib=rb-4.0.3&auto=format&fit=crop&w=1350&q=80" alt="Париж" class="branch-image">
            <div class="branch-overlay">
                <h3>Париж</h3>
                <p>Европейский центр инноваций</p>
                <a href="/branches/Paris" class="btn" style="padding: 0.5rem 1rem; font-size: 0.9rem; margin-top: 0.5rem;">Подробнее</a>
            </div>
        </div>
        
        <div class="card branch-card">
            <img src="https://images.unsplash.com/photo-1587330979470-3595ac045ab0?ixlib=rb-4.0.3&auto=format&fit=crop&w=1350&q=80" alt="Берлин" class="branch-image">
            <div class="branch-overlay">
                <h3>Берлин</h3>
                <p>Современный технологический хаб</p>
                <a href="/branches/Berlin" class="btn" style="padding: 0.5rem 1rem; font-size: 0.9rem; margin-top: 0.5rem;">Подробнее</a>
            </div>
        </div>
    </div>
    
    <div class="quick-links">
        <h3>Дополнительная информация</h3>
        <ul>
            <li><a href="/news">Новости о наших филиалах</a></li>
            <li><a href="/management">Руководство филиалов</a></li>
            <li><a href="/contacts">Контактная информация</a></li>
        </ul>
    </div>
    """
    return HTMLResponse(content=get_base_html("Филиалы", content))

@app.get("/branches/{city}", response_class=HTMLResponse)
async def branch_detail(city: str):
    branches = {
        "London": {
            "title": "Лондонский филиал",
            "address": "123 Business Street, London, UK",
            "phone": "+44 20 7946 0958",
            "email": "london@company.com",
            "description": "Наш первый международный филиал, открытый в 2015 году. Лондонский офис специализируется на финансовых технологиях и обслуживании клиентов из Европы и Ближнего Востока.",
            "image": "https://images.unsplash.com/photo-1513635269975-59663e0ac1ad?ixlib=rb-4.0.3&auto=format&fit=crop&w=1350&q=80",
            "manager": "Джон Смит",
            "employees": "45 сотрудников",
            "services": "Финансовые технологии, Консалтинг, Поддержка клиентов"
        },
        "Paris": {
            "title": "Парижский филиал",
            "address": "456 Rue de Commerce, Paris, France",
            "phone": "+33 1 23 45 67 89",
            "email": "paris@company.com",
            "description": "Европейский центр инноваций, открыт в 2018 году. Парижская команда сосредоточена на разработке новых продуктов и искусственном интеллекте.",
            "image": "https://images.unsplash.com/photo-1431274172761-fca41d930114?ixlib=rb-4.0.3&auto=format&fit=crop&w=1350&q=80",
            "manager": "Мари Дюпон",
            "employees": "32 сотрудника",
            "services": "Исследования и разработки, Искусственный интеллект, Продуктовая разработка"
        },
        "Berlin": {
            "title": "Берлинский филиал",
            "address": "789 Geschäftsstraße, Berlin, Germany",
            "phone": "+49 30 901820",
            "email": "berlin@company.com",
            "description": "Современный технологический хаб, открыт в 2020 году. Берлинский офис является центром разработки облачных решений и кибербезопасности.",
            "image": "https://images.unsplash.com/photo-1587330979470-3595ac045ab0?ixlib=rb-4.0.3&auto=format&fit=crop&w=1350&q=80",
            "manager": "Томас Мюллер",
            "employees": "28 сотрудников",
            "services": "Облачные решения, Кибербезопасность, Техническая поддержка"
        }
    }
    
    if city in branches:
        branch = branches[city]
        content = f"""
        <div class="card" style="position: relative; overflow: hidden; padding: 0;">
            <img src="{branch['image']}" alt="{branch['title']}" style="width: 100%; height: 400px; object-fit: cover;">
            <div style="position: absolute; bottom: 0; left: 0; right: 0; background: linear-gradient(transparent, rgba(0, 0, 0, 0.8)); padding: 2rem; color: white;">
                <h1 style="color: white;">{branch['title']}</h1>
            </div>
        </div>
        
        <div class="grid" style="margin-top: 2rem; grid-template-columns: 1fr 1fr;">
            <div class="card">
                <h2>Контактная информация</h2>
                <p><strong>Адрес:</strong> {branch['address']}</p>
                <p><strong>Телефон:</strong> {branch['phone']}</p>
                <p><strong>Email:</strong> {branch['email']}</p>
                <p><strong>Менеджер филиала:</strong> {branch['manager']}</p>
                <p><strong>Количество сотрудников:</strong> {branch['employees']}</p>
                <a href="/contacts" class="btn" style="padding: 0.5rem 1rem; font-size: 0.9rem; margin-top: 1rem;">Связаться с нами</a>
            </div>
            
            <div class="card">
                <h2>О филиале</h2>
                <p>{branch['description']}</p>
                <h3 style="margin-top: 1.5rem;">Основные направления</h3>
                <p>{branch['services']}</p>
                <a href="/branches" class="btn btn-secondary" style="padding: 0.5rem 1rem; font-size: 0.9rem; margin-top: 1rem;">Все филиалы</a>
            </div>
        </div>
        
        <div class="quick-links">
            <h3>Другие филиалы</h3>
            <ul>
                <li><a href="/branches/London">Лондон</a></li>
                                <li><a href="/branches/Paris">Париж</a></li>
                <li><a href="/branches/Berlin">Берлин</a></li>
            </ul>
        </div>
        
        <div class="card">
            <h2>Форма для связи с филиалом</h2>
            <form style="display: grid; gap: 1rem; margin-top: 1rem;">
                <div>
                    <label for="name" style="display: block; margin-bottom: 0.5rem; font-weight: 500;">Ваше имя</label>
                    <input type="text" id="name" style="width: 100%; padding: 0.7rem; border: 1px solid var(--gray); border-radius: 0.5rem;">
                </div>
                <div>
                    <label for="email" style="display: block; margin-bottom: 0.5rem; font-weight: 500;">Email</label>
                    <input type="email" id="email" style="width: 100%; padding: 0.7rem; border: 1px solid var(--gray); border-radius: 0.5rem;">
                </div>
                <div>
                    <label for="message" style="display: block; margin-bottom: 0.5rem; font-weight: 500;">Сообщение</label>
                    <textarea id="message" rows="4" style="width: 100%; padding: 0.7rem; border: 1px solid var(--gray); border-radius: 0.5rem;"></textarea>
                </div>
                <button type="submit" class="btn">Отправить</button>
            </form>
        </div>
        """
        return HTMLResponse(content=get_base_html(branch['title'], content))
    else:
        content = """
        <div class="card" style="text-align: center; padding: 3rem;">
            <h2>Филиал не найден</h2>
            <p style="margin: 1rem 0 2rem;">Запрошенный вами филиал не существует или был перемещен.</p>
            <a href="/branches" class="btn">Все наши филиалы</a>
        </div>
        """
        return HTMLResponse(content=get_base_html("Филиал не найден", content))


@app.get("/api/random")
async def random_number():
    return {"number": random.randint(1, 100)}

# Добавим обработку пользовательского агента
@app.get("/api/user-agent")
async def read_user_agent(request: Request):
    user_agent = request.headers.get("user-agent")
    return {"user_agent": user_agent}

# Добавим страницу 404 для несуществующих маршрутов
@app.exception_handler(404)
async def not_found_exception_handler(request: Request, exc):
    content = """
    <div class="hero" style="text-align: center;">
        <h1 style="color: white;">404 - Страница не найдена</h1>
        <p style="font-size: 1.2rem; margin: 1rem 0 2rem;">Запрошенная вами страница не существует или была перемещена.</p>
        <a href="/" class="btn">На главную</a>
    </div>
    
    <div class="quick-links">
        <h3>Возможно, вы искали:</h3>
        <ul>
            <li><a href="/news">Новости компании</a></li>
            <li><a href="/about">О компании</a></li>
            <li><a href="/contacts">Контакты</a></li>
            <li><a href="/branches">Наши филиалы</a></li>
        </ul>
    </div>
    """
    return HTMLResponse(content=get_base_html("Страница не найдена", content))


uvicorn.run(app)