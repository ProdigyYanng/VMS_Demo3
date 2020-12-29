"""Django settings for Demo2 project.Generated by 'django-admin startproject' using Django 2.2.For more information on this file, seehttps://docs.djangoproject.com/en/2.2/topics/settings/For the full list of settings and their values, seehttps://docs.djangoproject.com/en/2.2/ref/settings/"""import os# Build paths inside the project like this: os.path.join(BASE_DIR, ...)BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))# Quick-start development settings - unsuitable for production# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/# SECURITY WARNING: keep the secret key used in production secret!SECRET_KEY = 'z=7r0y=lf9&2a9!1!#eo-m19w(3e1u$pg+n=#4f=0)0ffzxh5s'# SECURITY WARNING: don't run with debug turned on in production!DEBUG = TrueALLOWED_HOSTS = ['*']# Application definitionINSTALLED_APPS = [  # Todo 完成！ 这里要加3个app 分别是登录页、管理员首页+管理员修改页、用户首页  具体见数据表.xlsx    'django.contrib.admin',    'login',    'controller',    'user',    'django.contrib.auth',    'django.contrib.contenttypes',    'django.contrib.sessions',    'django.contrib.messages',    'django.contrib.staticfiles',]MIDDLEWARE = [    'django.middleware.security.SecurityMiddleware',    'django.contrib.sessions.middleware.SessionMiddleware',    'django.middleware.common.CommonMiddleware',    'django.middleware.csrf.CsrfViewMiddleware',    'django.contrib.auth.middleware.AuthenticationMiddleware',    'django.contrib.messages.middleware.MessageMiddleware',    'django.middleware.clickjacking.XFrameOptionsMiddleware',]ROOT_URLCONF = 'Demo2.urls'TEMPLATES = [    {        'BACKEND': 'django.template.backends.django.DjangoTemplates',        'DIRS': [],  # 如果文件夹设置好了就不需要在这里设置，django会自动进行寻找        'APP_DIRS': True,        'OPTIONS': {            'context_processors': [                'django.template.context_processors.debug',                'django.template.context_processors.request',                'django.contrib.auth.context_processors.auth',                'django.contrib.messages.context_processors.messages',            ],        },    },]WSGI_APPLICATION = 'Demo2.wsgi.application'# Database# https://docs.djangoproject.com/en/2.2/ref/settings/#databasesDATABASES = {    'default': {        'ENGINE': 'sql_server.pyodbc',        'NAME': 'demo1',        'USER': 'root1',        'PASSWORD': '123456',        'HOST': '127.0.0.1',        'PORT': '1433',        'OPTIONS': {            'driver': 'ODBC Driver 13 for SQL Server',        },    }}# Password validation# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validatorsAUTH_PASSWORD_VALIDATORS = [    {        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',    },    {        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',    },    {        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',    },    {        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',    },]# Internationalization# https://docs.djangoproject.com/en/2.2/topics/i18n/LANGUAGE_CODE = 'zh-hans'TIME_ZONE = 'Asia/Shanghai'USE_I18N = TrueUSE_L10N = TrueUSE_TZ = True# Static files (CSS, JavaScript, Images)# https://docs.djangoproject.com/en/2.2/howto/static-files/STATIC_URL = '/static/'# LOGIN_URL = '//'# LOGIN_REDIRECT_URL = '/controller/'