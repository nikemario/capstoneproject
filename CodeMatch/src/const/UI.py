class UI:
    # # # # # # # # # # # # # #
    # LAYOUT DESIGN CONSTANTS #
    # # # # # # # # # # # # # #

    # Colors
    background = "#FFFFFF"
    foreground = "#000000"

    shadow = "#EEEEEE"
    overcast = "#666666"

    light_accent = "#FFFFFF"
    bright_accent = "#FFFFFF"
    rich_accent = "#FFFFFF"
    dark_accent = "#FFFFFF"

    external_padding = 20
    internal_padding = 5

    # Frame Padding
    frame_padding = {'padx': external_padding, 'pady': external_padding}

    frame_arch_padding = {'padx': external_padding,
                          'pady': (external_padding, internal_padding)}
    frame_u_padding = {'padx': external_padding,
                       'pady': (external_padding, internal_padding)}
    frame_c_padding = {'padx': (external_padding, internal_padding),
                       'pady': (external_padding, external_padding)}
    frame_d_padding = {'padx': (internal_padding, external_padding),
                       'pady': (external_padding, external_padding)}

    frame_top_padding = {'padx': internal_padding,
                         'pady': (external_padding, internal_padding)}
    frame_topleft_padding = {'padx': (external_padding, internal_padding),
                             'pady': (external_padding, internal_padding)}
    frame_topright_padding = {'padx': (internal_padding, external_padding),
                              'pady': (external_padding, internal_padding)}

    frame_bottom_padding = {'padx': internal_padding,
                            'pady': (internal_padding, external_padding)}
    frame_bottomleft_padding = {'padx': (external_padding, internal_padding),
                                'pady': (internal_padding, external_padding)}
    frame_bottomright_padding = {'padx': (internal_padding, external_padding),
                                 'pady': (internal_padding, external_padding)}

    # Widget Padding

    padding = {'padx': internal_padding, 'pady': internal_padding}

    ipadding = {'ipadx': internal_padding, 'ipady': internal_padding}
