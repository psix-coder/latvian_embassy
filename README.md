# 🏛️ Embassy Meeting Booking System

![Python](https://img.shields.io/badge/python-3.10+-blue.svg)
![Django](https://img.shields.io/badge/django-5.2-green.svg)
![DRF](https://img.shields.io/badge/DRF-3.14-red.svg)
![JWT](https://img.shields.io/badge/JWT-Auth-orange.svg)
![License](https://img.shields.io/badge/license-MIT-blue.svg)

> Django REST Framework asosida yaratilgan elchilik xizmatlari uchun online uchrashuv bron qilish tizimi

## 📖 Loyiha haqida

Embassy Meeting Booking System - bu elchiliklar, konsulliklar va davlat muassasalari uchun mo'ljallangan zamonaviy uchrashuv bron qilish va boshqarish tizimi. Loyiha Django REST Framework yordamida yaratilgan va JWT autentifikatsiya bilan himoyalangan RESTful API'ni taqdim etadi.

## ✨ Asosiy xususiyatlar

### 🔐 Autentifikatsiya va Xavfsizlik
- ✅ **JWT Authentication** - JWT token asosidagi xavfsiz autentifikatsiya
- ✅ **Custom User Model** - telefon raqami bilan kengaytirilgan foydalanuvchi modeli
- ✅ **Registration & Login** - dj-rest-auth orqali ro'yxatdan o'tish va kirish
- ✅ **Token Refresh** - avtomatik token yangilash
- ✅ **Allauth Integration** - Django-allauth integratsiyasi

### 📅 Uchrashuv Boshqaruvi
- ✅ **Service Management** - turli xizmatlarni yaratish va boshqarish
- ✅ **Meeting Booking** - uchrashuv bron qilish tizimi
- ✅ **User-specific Meetings** - har bir foydalanuvchi faqat o'z uchrashuvlarini ko'radi
- ✅ **DateTime Management** - sana va vaqt bilan ishlash
- ✅ **Auto Slug Generation** - xizmatlar uchun avtomatik slug yaratish

### 🎯 REST API
- ✅ **ViewSet Architecture** - Django REST Framework ViewSet'lari
- ✅ **CRUD Operations** - to'liq CRUD operatsiyalari
- ✅ **Serializers** - ma'lumotlarni serializatsiya qilish
- ✅ **Permissions** - kirish huquqlarini boshqarish
- ✅ **Filtering** - foydalanuvchiga tegishli ma'lumotlarni filtrlash

## 🛠️ Texnologiyalar

<div align="left">
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python"/>
  <img src="https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white" alt="Django"/>
  <img src="https://img.shields.io/badge/DRF-ff1709?style=for-the-badge&logo=django&logoColor=white" alt="Django REST Framework"/>
  <img src="https://img.shields.io/badge/JWT-000000?style=for-the-badge&logo=JSON%20web%20tokens&logoColor=white" alt="JWT"/>
  <img src="https://img.shields.io/badge/SQLite-07405E?style=for-the-badge&logo=sqlite&logoColor=white" alt="SQLite"/>
</div>

### Backend Stack
- **Python 3.10+**
- **Django 5.2.6**
- **Django REST Framework** - RESTful API yaratish
- **dj-rest-auth** - Authentication endpoints
- **django-allauth** - Ro'yxatdan o'tish va autentifikatsiya
- **Simple JWT** - JWT token management
- **SQLite3** - Ma'lumotlar bazasi (development)

## 🚀 O'rnatish va ishga tushirish

### Talablar

```
Python 3.10+
pip (Python package manager)
virtualenv (tavsiya etiladi)
```

### 1️⃣ Repository'ni clone qiling

```bash
git clone https://github.com/psix-coder/embassy-booking-system.git
cd embassy-booking-system
```

### 2️⃣ Virtual environment yarating

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Linux/Mac
python3 -m venv venv
source venv/bin/activate
```

### 3️⃣ Kerakli paketlarni o'rnating

```bash
pip install django
pip install djangorestframework
pip install dj-rest-auth
pip install django-allauth
pip install djangorestframework-simplejwt
```

Yoki requirements.txt fayl yarating va o'rnating:
```bash
pip install -r requirements.txt
```

### 4️⃣ Ma'lumotlar bazasini sozlang

```bash
python manage.py migrate
```

### 5️⃣ Superuser yarating

```bash
python manage.py createsuperuser
```

### 6️⃣ Serverni ishga tushiring

```bash
python manage.py runserver
```

Server manzili: `http://127.0.0.1:8000/`

## 📁 Loyiha strukturasi

```
embassy-booking-system/
├── accounts/                   # Custom user authentication
│   ├── models.py              # CustomUser model
│   ├── admin.py               # Admin configuration
│   └── migrations/            # Database migrations
├── embassy/                   # Main application
│   ├── models.py              # Service & Meeting models
│   ├── serializers.py         # DRF serializers
│   ├── views.py               # ViewSets
│   ├── urls.py                # URL routing
│   └── admin.py               # Admin panel
├── config/                    # Project configuration
│   ├── settings.py            # Django settings
│   ├── urls.py                # Root URL config
│   └── wsgi.py                # WSGI config
├── db.sqlite3                 # SQLite database
├── manage.py                  # Django management
└── README.md                  # Documentation
```

## 🗄️ Ma'lumotlar bazasi modellari

### CustomUser (accounts)
```python
- id (AutoField)
- username (CharField, unique)
- first_name (CharField)
- last_name (CharField)
- email (EmailField)
- phone_number (CharField, unique)  # Qo'shimcha maydon
- password (CharField)
- is_active (BooleanField)
- is_staff (BooleanField)
- date_joined (DateTimeField)
```

### Service (embassy)
```python
- id (AutoField)
- title (CharField, max_length=255)
- slug (SlugField, unique, auto-generated)
```

### Meeting (embassy)
```python
- id (AutoField)
- customer (ForeignKey → CustomUser)
- service (ForeignKey → Service)
- meet_time (DateTimeField)
- created_at (DateTimeField, auto_now_add)
```

## 🔌 API Endpoints

### Authentication Endpoints

| Method | Endpoint | Tavsif | Auth Required |
|--------|----------|--------|---------------|
| POST | `/dj-rest-auth/registration/` | Ro'yxatdan o'tish | ❌ |
| POST | `/dj-rest-auth/login/` | Tizimga kirish | ❌ |
| POST | `/dj-rest-auth/logout/` | Tizimdan chiqish | ✅ |
| GET | `/dj-rest-auth/user/` | Foydalanuvchi ma'lumotlari | ✅ |
| POST | `/dj-rest-auth/token/refresh/` | Token yangilash | ✅ |

### Service Endpoints

| Method | Endpoint | Tavsif | Auth Required |
|--------|----------|--------|---------------|
| GET | `/dashboard/services/` | Barcha xizmatlar ro'yxati | ✅ |
| POST | `/dashboard/services/` | Yangi xizmat yaratish | ✅ (Admin) |
| GET | `/dashboard/services/{slug}/` | Xizmat tafsilotlari | ✅ |
| PUT | `/dashboard/services/{slug}/` | Xizmatni yangilash | ✅ (Admin) |
| DELETE | `/dashboard/services/{slug}/` | Xizmatni o'chirish | ✅ (Admin) |

### Meeting Endpoints

| Method | Endpoint | Tavsif | Auth Required |
|--------|----------|--------|---------------|
| GET | `/dashboard/meetings/` | Mening uchrashuvlarim | ✅ |
| POST | `/dashboard/meetings/` | Uchrashuv bron qilish | ✅ |
| GET | `/dashboard/meetings/{id}/` | Uchrashuv tafsilotlari | ✅ |
| PUT | `/dashboard/meetings/{id}/` | Uchrashuvni yangilash | ✅ |
| DELETE | `/dashboard/meetings/{id}/` | Uchrashuvni bekor qilish | ✅ |

## 💡 API Foydalanish Misollari

### Ro'yxatdan o'tish

```bash
curl -X POST http://127.0.0.1:8000/dj-rest-auth/registration/ \
  -H "Content-Type: application/json" \
  -d '{
    "username": "john_doe",
    "email": "john@example.com",
    "password1": "securepass123",
    "password2": "securepass123",
    "phone_number": "+998901234567"
  }'
```

### Tizimga kirish

```bash
curl -X POST http://127.0.0.1:8000/dj-rest-auth/login/ \
  -H "Content-Type: application/json" \
  -d '{
    "username": "john_doe",
    "password": "securepass123"
  }'
```

**Response:**
```json
{
  "access": "eyJ0eXAiOiJKV1QiLCJhbGc...",
  "refresh": "eyJ0eXAiOiJKV1QiLCJhbGc...",
  "user": {
    "id": 1,
    "username": "john_doe",
    "email": "john@example.com"
  }
}
```

### Uchrashuv bron qilish

```bash
curl -X POST http://127.0.0.1:8000/dashboard/meetings/ \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "meet_time": "2025-10-15T14:30:00Z",
    "service": 1
  }'
```

### Xizmatlar ro'yxati

```bash
curl -X GET http://127.0.0.1:8000/dashboard/services/ \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN"
```

## ⚙️ Sozlamalar

### JWT Token Konfiguratsiyasi

```python
SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(minutes=60),   # 1 soat
    "REFRESH_TOKEN_LIFETIME": timedelta(days=7),      # 7 kun
}
```

### REST Framework Settings

```python
REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": (
        'dj_rest_auth.jwt_auth.JWTCookieAuthentication',
    )
}
```

## 🔒 Xavfsizlik

- 🔐 JWT token asosida autentifikatsiya
- 🛡️ CSRF himoyasi
- 🔑 Parollar hash qilingan holda saqlanadi
- 👥 Har bir foydalanuvchi faqat o'z ma'lumotlarini ko'radi
- ⏱️ Token muddati tugashi bilan avtomatik yangilanadi

## 🧪 Testing

```bash
python manage.py test
```

## 📈 Kelajakdagi yangilanishlar

- [ ] Email tasdiqlash tizimi
- [ ] SMS bildirishnomalar
- [ ] Uchrashuv calendar integration
- [ ] Admin dashboard UI
- [ ] Fayllar yuklash (pasport, dokumentlar)
- [ ] PostgreSQL'ga o'tish (production)
- [ ] Docker containerization
- [ ] Nginx + Gunicorn deployment
- [ ] Redis caching
- [ ] Celery async tasks
- [ ] Payment integration
- [ ] Multi-language support
- [ ] Uchrashuv vaqti konfliktini tekshirish
- [ ] Waiting list tizimi

## 🤝 Hissa qo'shish

1. Fork qiling
2. Feature branch yarating (`git checkout -b feature/AmazingFeature`)
3. Commit qiling (`git commit -m 'Add some AmazingFeature'`)
4. Push qiling (`git push origin feature/AmazingFeature`)
5. Pull Request oching

## 🐛 Muammolar

Issues bo'limiga o'ting: [GitHub Issues](https://github.com/psix-coder/embassy-booking-system/issues)

## 📝 Litsenziya

Bu loyiha MIT litsenziyasi ostida tarqatiladi.

## 👤 Muallif

**Psix Coder**

- GitHub: [@psix-coder](https://github.com/psix-coder)
- Email: psix.coder@example.com

## 🙏 Minnatdorchilik

- Django va DRF jamoasiga
- dj-rest-auth va django-allauth dasturchilarga
- Open-source jamiyatiga

## 📚 Qo'shimcha resurlar

- [Django Documentation](https://docs.djangoproject.com/)
- [Django REST Framework](https://www.django-rest-framework.org/)
- [dj-rest-auth Docs](https://dj-rest-auth.readthedocs.io/)
- [Simple JWT](https://django-rest-framework-simplejwt.readthedocs.io/)

---

<div align="center">

**⭐ Agar loyiha foydali bo'lsa, star qo'yishni unutmang! ⭐**

Made with ❤️ and Django REST Framework by [Psix Coder](https://github.com/psix-coder)

**🏛️ Embassy Meeting Booking System - Zamonaviy uchrashuv boshqaruvi**

</div>
