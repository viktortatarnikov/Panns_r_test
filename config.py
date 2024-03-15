sample_rate = 32000
clip_samples = sample_rate * 30

mel_bins = 64
fmin = 50
fmax = 14000
window_size = 1024
hop_size = 320
window = 'hann'
pad_mode = 'reflect'
center = True
device = 'cuda'
ref = 1.0
amin = 1e-10
top_db = None

#labels = ['alarm_clock', 'cat', 'cat+background', 'cat+dog', 'cat+music',
#	 'cat+speech', 'cat_hissing', 'cat_purring', 'child_singing', 'child_speech',
#	 'cough', 'cry', 'crying_baby', 'dog+music', 'dog+speech', 'dog_barking', 'dog_garling',
#	 'dog_howling', 'fight', 'fight+background', 'fight+glass', 'fight+speech', 'footsteps',
#	 'glass', 'howling', 'knock', 'laugh', 'laugh+speech', 'ringtone', 'ringtone+speech',
#	 'screams', 'screams+background', 'screams+speech', 'shots', 'shots+speech', 'sneeze',
#	 'snoring', 'whistle']

labels = ['blues', 'classical', 'country', 'disco', 'hiphop', 'jazz', 'metal',
    'pop', 'reggae', 'rock']
    
lb_to_idx = {lb: idx for idx, lb in enumerate(labels)}
idx_to_lb = {idx: lb for idx, lb in enumerate(labels)}
classes_num = len(labels)
