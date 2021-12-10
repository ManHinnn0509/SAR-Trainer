ENEMY_COLLISION_RADIUS = 20

# --- Constants from SAR (Including modified constants)

BULLET_MOVE_SPEED = {
   "GunPistol": 135,
   "GunDualPistol": 135,
   "GunMagnum": 195,
   "GunDeagle": 215,
   "GunSilencedPistol": 135,
   "GunShotgun": 105,
   "GunJag7": 95,
   "GunSMG": 135,
   "GunThomas": 135,
   "GunAK": 172,
   "GunM16": 172,
   "GunDart": 133,
   "GunHuntingRifle": 250,
   "GunSniper": 250,
   "GunMinigun": 175,
   "GunBow": 170,
   "GunCrossbow": 155
}

WEAPON_CLIP_SIZE = {
    "GunPistol":10,
    "GunDualPistol":20,
    "GunMagnum":6,
    "GunDeagle":8,
    "GunSilencedPistol":12,
    "GunShotgun":5,
    "GunJag7":5,
    "GunSMG":25,
    "GunThomas":40,
    "GunAK":30,
    "GunM16":30,
    "GunDart":6,
    "GunHuntingRifle":1,
    "GunSniper":5,
    "GunMinigun":100,
    "GunBow":1,
    "GunCrossbow":4
}

WEAPON_ID_LIST = list(BULLET_MOVE_SPEED.keys())

PLAYER_MAX_MOVE_SPEED_NORMAL = 31 / 100