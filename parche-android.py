# Permisos de avisos y firma fija (lo corre GitHub al compilar)
import base64
m='android/app/src/main/AndroidManifest.xml'
s=open(m,encoding='utf-8').read()
perms=['POST_NOTIFICATIONS','SCHEDULE_EXACT_ALARM','RECEIVE_BOOT_COMPLETED','WAKE_LOCK','VIBRATE']
extra=''.join(f'\n    <uses-permission android:name="android.permission.{p}" />' for p in perms if f'android.permission.{p}"' not in s)
s=s.replace('<uses-permission android:name="android.permission.INTERNET" />','<uses-permission android:name="android.permission.INTERNET" />'+extra,1)
open(m,'w',encoding='utf-8').write(s)
open('android/firma.keystore','wb').write(base64.b64decode(open('firma.txt').read()))
g='android/app/build.gradle'
gs=open(g,encoding='utf-8').read()
if 'firma.keystore' not in gs:
    gs=gs.replace('android {','''android {
    signingConfigs {
        debug {
            storeFile file("${rootDir}/firma.keystore")
            storePassword "android"
            keyAlias "androiddebugkey"
            keyPassword "android"
        }
    }''',1)
    open(g,'w',encoding='utf-8').write(gs)
print('permisos y firma listos')
