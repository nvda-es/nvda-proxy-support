# NVDA için Proxy Desteği #

* Yazan: Jose Manuel Delicado
* NVDA uyumluluğu: 2023.3.4 ve sonrası
* [kararlı sürüm][1] indir

Bu eklenti, NVDA ekran okuyucusunun bir veya daha fazla proxy sunucusu
aracılığıyla İnternet'e bağlanmasına olanak tanır. Bunu mümkün kılmak için,
standart Python kitaplığına çeşitli yamalar uygular veya seçilen
konfigürasyona bağlı olarak belirli ortam değişkenlerini değiştirir. NVDA'yı
ve eklentilerini kurumsal ortamınızdan otomatik olarak güncelleyebilecek ve
hatta kuruluş proxy sunucunuzun izin vermesi koşuluyla uzak oturumlar
gerçekleştirebileceksiniz.

## Özellikler

* Çeşitli proxy sunucu türleri için destek: http, çorap4 ve çorap5.
* Tüm trafiği proxy sunucusu veya yalnızca belirli trafik (http, https, ftp)
  üzerinden yeniden yönlendirme yeteneği.
* Tüm trafiği bir proxy sunucusu üzerinden yeniden yönlendirme ve ardından
  belirli trafiği diğer sunucular (iç içe geçmiş proxy'ler) üzerinden
  yeniden yönlendirme yeteneği.
* Profil değiştirme ve yapılandırma sıfırlama farkındalığı: Genellikle
  NVDA'nın taşınabilir bir kopyasıyla çalışıyorsanız, farklı ortamlar (ev,
  iş, ofis1, ofis2) için çeşitli profiller oluşturabilir ve bunları manuel
  olarak etkinleştirebilirsiniz.

## Kullanım

This add-on adds a new category to the NVDA settings dialog called
"Proxy". In this category, you will find four settings groups. The first one
allows you to configure a general proxy for all traffic. The other groups
allow you to configure proxy servers only for specific protocols. All groups
have the following fields:

* Host: hostname or ip address of the proxy server. Leave empty to disable
  that particular proxy.
* Bağlantı noktası: sunucu bağlantı noktası.
* Kullanıcı adı: isteğe bağlı. Sunucu yetkilendirmesi için kullanıcı adı.
* Şifre: isteğe bağlı. Sunucu yetkilendirmesi için parola. Socks4 sunucuları
  için şifre gerekmediğini unutmayın.

Önceki alanlara ek olarak, ilk ayarlar grubunda aşağıdaki seçenekler
mevcuttur:

* SOCKS proxy tipi: çorap4, çorap5 veya http seçilebilir.
* Mümkünse dns istekleri için proxy kullan: Bu onay kutusu işaretlendiğinde,
  ana bilgisayar adları veya alan adları doğrudan proxy sunucusuna
  gönderilir ve burada çözümlenir. İşareti kaldırıldığında, isimler yerel
  olarak çözülecek ve sunucu sadece hedef ip adresini alacaktır. Tüm stock4
  proxy sunucularının bu seçeneği desteklemediğini unutmayın.

Genellikle çoğu kullanıcının yalnızca ilk ayar grubunu yapılandırması
gerekir. Proxy ayrıntılarınızı bilmiyorsanız, daha fazla bilgi için kuruluş
ağ yöneticinize danışın.

## Sınırlamalar

* Çok sınırlı IPV6 desteği.
* UDP trafiği tüm proxy sunucularında desteklenmez.
* Harici DLL kitaplıkları bu eklentide yapılandırılan ayarlara uymaz.
* Http proxy sunucuları için yalnızca temel kimlik doğrulama
  desteklenir. Özet kimlik doğrulaması desteklenmiyor.
* Tüm trafiği (https bağlantıları dahil) bir http proxy üzerinden yeniden
  yönlendirmek için sunucunun CONNECT http yöntemini desteklemesi gerekir.
* Bir "doğrudan bağlantı" modu yapılandırılamaz. Belirli bir proxy'yi devre
  dışı bırakırsanız, bunun yerine sistem varsayılanı kullanılır.

## Changelog

### Sürüm 1.2

* NVDA 2023.1 ile uyumludur.
* Güvenlik sebeplerinden dolayı minimum NVDA sürümü 2022.4'e ayarlanmıştır.
* Çeviriler güncellendi.

### Sürüm 1.1

* NVDA 2022.1 ile uyumludur.
* Güvenlik sebeplerinden dolayı minimum NVDA sürümü 2021.1'e ayarlanmıştır.
* "Mümkünse dns istekleri için proxy kullan" onay kutusu işaretlendiğinde ve
  genel bir proxy yapılandırıldığında socket.getaddrinfo işlevini yama.

### Sürüm 1.0

* İlk Sürüm.

[[!tag dev stable]]

[1]: https://www.nvaccess.org/addonStore/legacy?file=proxy
