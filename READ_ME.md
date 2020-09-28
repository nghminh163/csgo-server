# Cài đặt
- Sửa file .env để config (Bổ sung SRCDS_TOKEN)
- Chạy run.py
- Check logs của container `csgo-dedicated` cho đến khi download xong và đang run server (Vào game để check)
- Stop container `csgo-dedicated`
- Chạy `install_sm.py`
- Start container `csgo-dedicated` và attach vào. Sau khi run xong gõ `meta list` và `sm list` để kiểm tra. =)) lên là được
- Chạy file `install_ptah.py` và làm theo hướng dẫn khi file run xong
- Chạy file `insta_mod_weapon.py` và làm theo hướng dẫn khi file run xong
- Vào file `csgo-data/csgo/addons/sourcemod/configs/core.cfg` sửa `FollowCSGOServerGuidelines` thành `no`
- Chạy file `install_mod_glove.py` và làm theo hướng dẫn khi file run xong
- Chạy file `install_mod_agent.py` và làm theo hướng dẫn khi file run xong

### Admin
- Lấy steam ID tại link [sau](https://steamid.io/lookup/76561198840401588) và lấy SteamID có format `STEAM_0:0:ID`, sau đó sửa file admins_simple.ini bằng cách tạo dòng mới và thay bằng `"yoursteamid":"99:z"` và chạy file `admin.py`