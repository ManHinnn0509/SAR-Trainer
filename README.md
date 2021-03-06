# SAR-Trainer <a href='#'><img src='./img/dr_beagle/dr_beagle_head.png' align="right" height="138.5" /></a>

SAR simulator for practicing aiming &amp; shooting

Default weapon: Magnum

Note: I DO NOT own the artworks / audios used in this project

P.S: This is my first time developing game like applications with Pygame :P

## Demo

![init](./img/demo/init.png)

## Configuration

There are some options can be configurated in [config.py](./config.py)

Like: 

* Window size
* Volume
* Images of player, cursor, background and enemies
* Maximum enemy amount per time
* Infinite ammo

## Planned

I divided them into different categories

### UI

* [x] [Add status display on top-left corner (Fired bullets amount, kills, hit rate)](https://github.com/ManHinnn0509/SAR-Trainer/commit/513b867c0efbafbda7e3187e012dbd279c076073)

### Player

* [ ] Better moving speed
* [ ] Fix character in the middle when moving around

### Enemies

* [ ] Better spawning mechanism
* [ ] Make enemy moves

### Weapons

* [ ] Better bullet speed
* [ ] Add recoil
* [x] [Add reload to weapon(s)](https://github.com/ManHinnn0509/SAR-Trainer/commit/9966ed697c7f61d9a28fb765e7a619fc77dd772d)
* [ ] Add more weapons
* [ ] Add full-auto weapons
* [ ] Add cooldown on specific wepaons (E.g: Magnum)

### Ultimate goals

* [ ] Remake with camera that follows the player (Player always be in the center)
* [ ] Re-create this in Unity / C#