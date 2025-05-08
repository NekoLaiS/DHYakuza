init -3 python:
    ## Dynamic Super Position (DSP)
    # DSP is a feature in where the game upscales the positions of assets 
    # with higher resolutions (1080p).
    # This is just simple division from Adobe, implemented in Python.
    def dsp(orig_val):
        ceil = not isinstance(orig_val, float)
        dsp_scale = config.screen_width / 1280.0 
        if ceil: return math.ceil(orig_val * dsp_scale)
        # since `absolute * float` -> `float`
        # we wanna keep the same type
        return type(orig_val)(orig_val * dsp_scale)
    
    # This makes evaluating the value faster
    renpy.pure(dsp)

    ## Dynamic Super Resolution
    # DSR is a feature in where the game upscales asset sizes to higher
    # resolutions (1080p) and sends back a modified transform.
    # (Recommend that you just make higher res assets than upscale lower res ones)
    def dsr(path):
        img_bounds = renpy.image_size(path)
        return Transform(path, size=(dsp(img_bounds[0]), dsp(img_bounds[1])))