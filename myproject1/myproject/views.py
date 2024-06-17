from django.shortcuts import render
from berita.models import Artikel, Kategori

def home(request):
    template_name = "halaman/index.html"
    kategori = request.GET.get('kategori')
    if kategori == None:
        print("ALL")
        data_artikel = Artikel.objects.all()
    else:
        # try:
        #     print("Buka ALL")
        #     get_kategori = Kategori.objects.get(nama=kategori)
        #     data_artikel = Artikel.objects.filter(kategori=get_kategori)
        # except:
        #     data_artikel = []
        get_kategori = Kategori.objects.filter(nama=kategori)
        if get_kategori.count() != 0:
            data_artikel = Artikel.objects.filter(kategori=get_kategori[0])
        else:
            data_artikel =[]
    
    data_kategori = Kategori.objects.all()
    context = {
        'title' : 'Selamat Datang Di Web Saya',
        'data_artikel' : data_artikel,
        'data_kategori' : data_kategori,
    }
    return render(request, template_name, context)

def about(request):
    template_name = "halaman/about.html"
    context = {
        'title': 'Selamat datang di halaman about',
        'umur': 20,
        }
    return render(request, template_name, context)

def contact(request):
    template_name = "halaman/contact.html"
    context = {
        'title': 'Selamat datang di halaman contact',
        'umur': 20,
        }
    return render(request, template_name, context)

def profil(request):
    template_name = "halaman/profil.html"
    context = {
        'title': 'Selamat datang di halaman profil',
        'umur': 20,
        }
    return render(request, template_name, context)

def baru(request):
    template_name = "baru.html"
    return render(request, template_name)

def detail_artikel(request, slug):
    template_name = "halaman/detail_artikel.html"
    artikel = Artikel.objects.get(slug=slug)
    print(artikel)
    context = {
        'titel' : artikel.judul,
        'artikel' : artikel
    }
    return render(request, template_name, context)