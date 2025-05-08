
image raindrop_particle_large = "mod_assets/effects/raindrop_large.png"
image raindrop_particle_normal = "mod_assets/effects/raindrop_normal.png"
image raindrop_particle_small = "mod_assets/effects/raindrop_small.png"

image eff_light_rain:
    truecenter
    xzoom 1.3 yzoom 1.7
    contains:
        SnowBlossom("raindrop_particle_normal", 10, 50, (50, 100), (1500, 1600))
    contains:
        SnowBlossom("raindrop_particle_small", 25, 50, (25, 50), (1400, 1500))

image eff_light_rain_l:
    "eff_light_rain"
    rotate 16.0

image eff_light_rain_r:
    "eff_light_rain"
    rotate -16.0

image eff_rain:
    truecenter
    xzoom 1.3 yzoom 1.7
    contains:
        SnowBlossom("raindrop_particle_large", 10, 50, (75, 125), (1600, 1700))
    contains:
        SnowBlossom("raindrop_particle_normal", 25, 50, (50, 100), (1500, 1600))
    contains:
        SnowBlossom("raindrop_particle_small", 150, 50, (25, 50), (1400, 1500))

image eff_rain_l:
    "eff_rain"
    rotate 16.0

image eff_rain_r:
    "eff_rain"
    rotate -16.0

image eff_hard_rain:
    contains:
        "eff_rain"
    contains:
        "eff_rain"

image eff_hard_rain_l:
    contains:
        "eff_rain_l"
    contains:
        "eff_rain_l"

image eff_hard_rain_r:
    contains:
        "eff_rain_r"
    contains:
        "eff_rain_r"
            
image eff_light_rain:
    truecenter
    xzoom 1.3 yzoom 1.7
    contains:
        SnowBlossom("raindrop_particle_normal", 10, 50, (50, 100), (1500, 1600))
    contains:
        SnowBlossom("raindrop_particle_small", 25, 50, (25, 50), (1400, 1500))

image eff_light_rain_l:
    "eff_light_rain"
    rotate 16.0

image eff_light_rain_r:
    "eff_light_rain"
    rotate -16.0