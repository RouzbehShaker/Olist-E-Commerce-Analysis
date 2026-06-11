# IYU 228 - İş Yeri Uygulaması Projesi: Olist Veri Analizi

Bu proje, Ostim Teknik Üniversitesi IYU 228 İş Yeri Uygulaması dersi kapsamında hazırlanmıştır. Projede Brezilya e-ticaret platformu Olist'in veri seti kullanılarak veritabanı yönetimi ve veri analizi yapılmıştır.

## Kullanılan Teknolojiler
- **Python:** Verileri okumak ve grafik çizmek için (Pandas, Matplotlib, Seaborn).
- **SQL (SQLite):** Tabloları oluşturmak, birbirine bağlamak ve veri analizi yapmak için.
- **GitHub:** Kodların saklanması ve versiyon kontrolü için.

## Proje Süreci ve Yapılanlar
İlk olarak Kaggle'dan indirdiğim `olist_customers_dataset.csv`, `olist_orders_dataset.csv` ve `olist_order_items_dataset.csv` dosyalarını Python ile okuyup SQLite veritabanına aktardım. Veritabanında tabloları ve aralarındaki bağlantıları (Foreign Key) kurdum. 

Daha sonra teslim edilen siparişleri filtreleyip, eyaletlere göre sipariş sayısını ve toplam ciroyu hesaplayan bir JOIN sorgusu yazdım. En son bu sorgudan dönen verileri Python ile çekip çubuk grafiği (bar chart) olarak görselleştirdim.

## Zorlanılan Kısımlar ve Öğrenilenler
Proje sürecinde en çok zorlandığım kısım CSV dosyalarındaki verileri SQL veritabanına aktarırken veri tiplerini uyumlu hale getirmek ve üç farklı tabloyu JOIN ile hatasız bir şekilde birleştirmekti. 

Bu proje sayesinde Python ve SQL dillerini aynı proje içinde entegre bir şekilde kullanmayı pratik ettim. Ayrıca kodlarımı GitHub'a yükleyerek versiyon kontrolü konusunda tecrübe kazandım.

## Nasıl Çalıştırılır?
1. Bu depoyu bilgisayarınıza indirin.
2. Bilgisayarınızda Python yüklü olmalıdır. Gerekli kütüphaneleri kurmak için terminale şu komutu yazın: 
   `pip install pandas matplotlib seaborn`
3. Kaggle'dan ilgili 3 adet CSV dosyasını indirip kodlarla aynı klasörün içine koyun.
4. Terminalden veya komut satırından `python veri_analizi.py` komutunu çalıştırın.
5. İşlem bitince kodların olduğu klasörde `olist_ecommerce.db` veritabanı dosyası ve `eyalet_ciro_analizi.png` adında bir grafik resmi otomatik olarak oluşacaktır.
