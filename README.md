
<center><h2>Yer İstasyonu Konum Optimizasyonu</h2></center>
Uyduların yer istasyonlarıyla iletişimini en verimli şekilde gerçekleştirmeleri için yer istasyonunun
konumlandırılması uydu haberleşmesinde oldukça önemli bir çalışma alanıdır. Bu projenin amacı
farklı yörüngelerdeki belirli sayıdaki uydu için, verilen link bütçesi hesaplamalarını göz önünde
bulundurarak istenilen bir coğrafi bölgede bulunması gereken yer istasyonu sayısını ve konumlarını
optimize edecek bir algoritma geliştirmek olacaktır.
<center><img src="https://upload.wikimedia.org/wikipedia/commons/d/de/2005-05-15-raisting_900x460.jpg" width="700" height="300"></center>


Uydu Konum Belirlenmesi
Yörünge İlerleticiler (Propagator)
Yörünge ilerleticiler, gözlemlenen başlangıç konumlarını kullanarak bir objenin uzayda gelecekteki hareket
durumunu tahmin etmek için kullanılan olasılıksal modellerdir.



Yer İstasyonu Üzerinden Geçiş (Acces)
Hesaplanması
Uydunun zamana bağlı uzaydaki konumu - Yer İstasyonuna göre zamana bağlı azimuth ve elevation açısı
- Yer istasyonunun Dünya üzerindeki konumu - Yer İstasyonunun uyduyu görebileceği LOS süresi



Challenge
Link bütçesi analizlerine göre uydularla kesintisiz iletişim 5 derece elevasyon üzerinde
başlamaktadır. 5 derece elevasyondan sonra bir uydu yer istasyonuna saniyede 0.2 mBla başlayıp
90 derece elevasyona kadar 3.6mB, lineer bir şekilde artan data indirebilme yeteneğine sahiptir.
Aşağıda yörünge parametreleri verilen uyduların hepsinin yukarıda belirtilen data indirme
donanımına sahip olduğu düşünülebilir. Amaç, bir haftalık bir analiz süresinde, Türkiye üzerine
konumlandırılacak en az yer istasyonuyla en çok datayı indirecek yer istasyonu dağılımını
sağlamaktır.
Analiz başlama zamanı : 4 Kasım 2022 15:00:00 UTC
Analiz bitiş zamanı : 11 Kasım 2022 15:00:00 UTC
