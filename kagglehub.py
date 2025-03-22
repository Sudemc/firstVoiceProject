import os
from spleeter.separator import Separator
import librosa
import librosa.display
import matplotlib.pyplot as plt
import numpy as np

# Müzik veri seti dizini
music_dataset_path = '/home/cucemen/Belgeler/miniproje/music_dataset/'

# Müzik veri setindeki tüm enstrüman klasörlerini listele
instrument_folders = [f for f in os.listdir(music_dataset_path) if os.path.isdir(os.path.join(music_dataset_path, f))]

if not instrument_folders:
    print("Hiç enstrüman klasörü bulunamadı!")
else:
    # Kullanıcıya enstrümanları seçmesi için seçenek sunma
    print("Enstrümanlar:")
    for idx, folder in enumerate(instrument_folders):
        print(f"{idx + 1}. {folder}")
    
    # Kullanıcının enstrüman seçmesini sağla
    choice = int(input("Bir enstrüman seçin (1-{}): ".format(len(instrument_folders))))

    # Seçilen enstrüman klasörünü al
    selected_instrument = instrument_folders[choice - 1]
    instrument_path = os.path.join(music_dataset_path, selected_instrument)

    # Seçilen enstrüman klasöründeki ilk ses dosyasını al
    audio_files = [f for f in os.listdir(instrument_path) if f.endswith('.wav')]

    if len(audio_files) == 0:
        print(f"{selected_instrument} klasöründe ses dosyası bulunamadı!")
    else:
        # İlk ses dosyasını seç
        selected_audio = audio_files[0]
        input_audio_path = os.path.join(instrument_path, selected_audio)
        output_path = '/home/cucemen/Belgeler/miniproje/output/621/'  # Ayrılmış ses dosyasının kaydedileceği çıkış yolu

        # Spleeter ile ses dosyasını ayırma
        separator = Separator('spleeter:2stems')  # Spleeter ile iki enstrüman ayırma (örneğin, şarkıcı ve arka plan müziği)
        try:
            print(f"{input_audio_path} dosyasını ayırmaya başlıyoruz...")
            separator.separate_to_file(input_audio_path, output_path)
            print(f"Ayrılmış dosyalar {output_path} dizinine kaydedildi.")
        except Exception as e:
            print(f"Bir hata oluştu: {e}")

        # Ayrılmış dosya yolları (vokal ve enstrümantal parçalar)
        vocals_path = os.path.join(output_path, 'vocals.wav')
        accompaniment_path = os.path.join(output_path, 'accompaniment.wav')

        # Dosyaların gerçekten var olduğunu kontrol et
        if not os.path.exists(vocals_path):
            print(f"Vokal dosyası bulunamadı: {vocals_path}")
        if not os.path.exists(accompaniment_path):
            print(f"Arka plan dosyası bulunamadı: {accompaniment_path}")

        # Eğer dosyalar varsa, yüklemeye devam et
        else:
            # Ses dosyasını yükle
            y_vocals, sr_vocals = librosa.load(vocals_path, sr=None)
            y_accompaniment, sr_accompaniment = librosa.load(accompaniment_path, sr=None)

            # Zaman eksenini oluştur
            t_vocals = librosa.times_like(y_vocals)
            t_accompaniment = librosa.times_like(y_accompaniment)

            # Grafik oluştur
            plt.figure(figsize=(12, 8))

            # Vokal sesi çiz
            plt.subplot(2, 1, 1)
            librosa.display.waveshow(y_vocals, sr=sr_vocals, alpha=0.7)
            plt.title(f'{selected_instrument} - Vocals')
            plt.xlabel('Time (s)')
            plt.ylabel('Amplitude')

            # Enstrümantal sesi çiz
            plt.subplot(2, 1, 2)
            librosa.display.waveshow(y_accompaniment, sr=sr_accompaniment, alpha=0.7)
            plt.title(f'{selected_instrument} - Accompaniment')
            plt.xlabel('Time (s)')
            plt.ylabel('Amplitude')

            # Grafik göster
            plt.tight_layout()
            plt.show()

            # Mel spektral özelliklerini hesapla
            S_vocals = librosa.feature.melspectrogram(y=y_vocals, sr=sr_vocals)
            S_accompaniment = librosa.feature.melspectrogram(y=y_accompaniment, sr=sr_accompaniment)

            # Mel spektral özelliklerini logaritmik hale getir
            S_vocals_db = librosa.power_to_db(S_vocals, ref=np.max)
            S_accompaniment_db = librosa.power_to_db(S_accompaniment, ref=np.max)

            # Grafik oluştur
            plt.figure(figsize=(14, 8))

            # Vokal spektrogramı çiz 
            plt.subplot(2, 1, 1)
            librosa.display.specshow(S_vocals_db, sr=sr_vocals, x_axis='time', y_axis='mel')
            plt.title(f'{selected_instrument} - Vocals Mel Spectrogram')
            plt.colorbar(format='%+2.0f dB')

            # Enstrümantal spektrogramı çiz
            plt.subplot(2, 1, 2)
            librosa.display.specshow(S_accompaniment_db, sr=sr_accompaniment, x_axis='time', y_axis='mel')
            plt.title(f'{selected_instrument} - Accompaniment Mel Spectrogram')
            plt.colorbar(format='%+2.0f dB')

            # Grafik göster
            plt.tight_layout()
            plt.show()


            # Kısa zamanlı Fourier dönüşümü
            D_vocals = librosa.stft(y_vocals)
            D_accompaniment = librosa.stft(y_accompaniment)

            # Frekans spektrumlarını logaritmik hale getir
            D_vocals_db = librosa.amplitude_to_db(np.abs(D_vocals), ref=np.max)
            D_accompaniment_db = librosa.amplitude_to_db(np.abs(D_accompaniment), ref=np.max)

            # Grafik oluştur
            plt.figure(figsize=(14, 8))

            # Vokal frekans spektrumunu çiz
            plt.subplot(2, 1, 1)
            librosa.display.specshow(D_vocals_db, sr=sr_vocals, x_axis='time', y_axis='log')
            plt.title(f'{selected_instrument} - Vocals Frequency Spectrum')
            plt.colorbar(format='%+2.0f dB')

            # Enstrümantal frekans spektrumunu çiz
            plt.subplot(2, 1, 2)
            librosa.display.specshow(D_accompaniment_db, sr=sr_accompaniment, x_axis='time', y_axis='log')
            plt.title(f'{selected_instrument} - Accompaniment Frequency Spectrum')
            plt.colorbar(format='%+2.0f dB')

            # Grafik göster
            plt.tight_layout()
            plt.show()


            # Zaman zarfını hesapla
            frame_length = 2048
            hop_length = 512
            y_vocals_env = librosa.onset.onset_strength(y=y_vocals, sr=sr_vocals, hop_length=hop_length)
            y_accompaniment_env = librosa.onset.onset_strength(y=y_accompaniment, sr=sr_accompaniment, hop_length=hop_length)

            # Grafik oluştur
            plt.figure(figsize=(14, 8))

            # Vokal zaman zarfını çiz
            plt.subplot(2, 1, 1)
            plt.plot(librosa.times_like(y_vocals_env, hop_length=hop_length), y_vocals_env, label='Vocals')
            plt.title(f'{selected_instrument} - Vocals Envelope')
            plt.xlabel('Time (s)')
            plt.ylabel('Amplitude')

            # Enstrümantal zaman zarfını çiz
            plt.subplot(2, 1, 2)
            plt.plot(librosa.times_like(y_accompaniment_env, hop_length=hop_length), y_accompaniment_env, label='Accompaniment', color='orange')
            plt.title(f'{selected_instrument} - Accompaniment Envelope')
            plt.xlabel('Time (s)')
            plt.ylabel('Amplitude')

            # Grafik göster
            plt.tight_layout()
            plt.show()

            # Pitch (frekans) tespiti
            f0_vocals, voiced_flag_vocals, voiced_probs_vocals = librosa.pyin(y_vocals, fmin=librosa.note_to_hz('C2'), fmax=librosa.note_to_hz('C7'))
            f0_accompaniment, voiced_flag_accompaniment, voiced_probs_accompaniment = librosa.pyin(y_accompaniment, fmin=librosa.note_to_hz('C2'), fmax=librosa.note_to_hz('C7'))

            # Grafik oluştur
            plt.figure(figsize=(14, 8))

            # Vokal pitch grafiği
            plt.subplot(2, 1, 1)
            plt.plot(librosa.times_like(f0_vocals), f0_vocals, label='Pitch')
            plt.title(f'{selected_instrument} - Vocals Pitch')
            plt.xlabel('Time (s)')
            plt.ylabel('Frequency (Hz)')

            # Enstrümantal pitch grafiği
            plt.subplot(2, 1, 2)
            plt.plot(librosa.times_like(f0_accompaniment), f0_accompaniment, label='Pitch', color='orange')
            plt.title(f'{selected_instrument} - Accompaniment Pitch')
            plt.xlabel('Time (s)')
            plt.ylabel('Frequency (Hz)')

            # Grafik göster
            plt.tight_layout()
            plt.show()
