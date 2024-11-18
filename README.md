# DataScaling
DataScaling is a project designed to explore and compare various strategies for efficiently handling and displaying large datasets. It focuses on identifying challenges and implementing solutions for data-heavy applications, ensuring optimal performance and usability at scale.

# Requirements
- [Python](https://www.python.org/downloads/)
- [Django](https://docs.djangoproject.com/en/5.1/topics/install/#installing-official-release)

# Features
- Database population generator
- Different ways of data representation
- Performance optimization (N+1)
- Caching mechanisms
- Searchbar

# Setup
1. **Clone the repository**
2. **Install dependencies**
   ```sh
   pip install -r requirements.txt
   ```
3. **Run database migrations**
   ```sh
   python manage.py migrate
   ```
4. **Run the development server**
   ```sh
   python manage.py runserver
   ```
# Sources
- [Django documentation](https://www.djangoproject.com/start/)
- [Faker documentation](https://faker.readthedocs.io/en/master/)
- [N+1 problem](https://dev.to/herchila/how-to-avoid-n1-queries-in-django-tips-and-solutions-2ajo)
- [Django Debug Toolbar documentation](https://django-debug-toolbar.readthedocs.io/en/latest/installation.html)
- [Data displaying possibilities](https://crocoblock.com/blog/pagination-vs-infinite-scroll/)
- [Caching Django](https://www.sitepoint.com/django-caching-comprehensive-guide/)
- [ChatGPT](https://chatgpt.com/share/673b6940-4318-8007-978d-7a304ac9a0a6)
