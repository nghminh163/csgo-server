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

### Hướng dẫn
##### [Weapon](https://forums.alliedmods.net/showthread.php?t=298770)
- Súng: !ws
- Nametag: !nametag
- Dao: !knife

##### [Găng](https://forums.alliedmods.net/showthread.php?t=298770)
- Găng: !gloves || !glove

##### [Nhân vật](https://forums.alliedmods.net/showthread.php?t=319964) Chưa test
- Nhân vật: !agents

##### [PUG](https://github.com/splewis/csgo-pug-setup) Chưa test
- Setup trận: !setup || !10man
- Ready: !ready
- Unready: !notready
- Dừng: !pause
- Bỏ dừng: !unpause
- Start: !start
- Set captain: !capt
- Set random captain: !rand
- Leader: !leader
- Dừng game: !endgame
- Buộc dừng game: !forceend
- Chuyển team và ở lại khi thắng round dao: !swap và !stay (Ví dụ ban đầu ở T thì thắng round dao có thể !stay để ở lại T hoặc !swap để sang CT) hoặc sử dụng !t và !ct

