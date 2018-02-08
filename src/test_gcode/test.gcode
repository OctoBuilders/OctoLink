M190 S60.000000
M109 S200.000000
;Sliced at: Wed 17-01-2018 10:28:04
;Basic settings: Layer height: 0.16 Walls: 1.2 Fill: 10
;Print time: 21 minutes
;Filament used: 1.167m 3.0g
;Filament cost: None
;M190 S60 ;Uncomment to add your own bed temperature line
;M109 S200 ;Uncomment to add your own temperature line
G21        ;metric values
G90        ;absolute positioning
M82        ;set extruder to absolute mode
M107       ;start with the fan off
G28 X0 Y0  ;move X/Y to min endstops
G28 Z0     ;move Z to min endstops
G1 Z15.0 F3600 ;move the platform down 15mm
G92 E0                  ;zero the extruded length
G1 F200 E3              ;extrude 3mm of feed stock
G92 E0                  ;zero the extruded length again
G1 F3600
;Put printing message on LCD screen
M117 Printing...

;Layer count: 1
;LAYER:0
M107
G0 F3600 X76.800 Y76.800 Z0.200
;TYPE:SKIRT
G1 F1500 X123.200 Y76.800 E1.54327
G1 X123.200 Y123.200 E3.08654
G1 X76.800 Y123.200 E4.62981
G1 F2700 X118.862 Y81.903 E1167.39467
G0 F3600 X118.862 Y81.339
G1 F2700 X118.660 Y81.136 E1167.40227
M107
G1 F3600 E1166.90227
G0 X118.660 Y81.136 Z7.500
;End GCode
M104 S0                     ;extruder heater off
M140 S0                     ;heated bed heater off (if you have it)
G91                                    ;relative positioning
G1 E-1 F300                            ;retract the filament a bit before lifting the nozzle, to release some of the pressure
G1 Z+0.5 E-5 X-20 Y-20 F3600 ;move Z up a bit and retract filament even more
G28 X0 Y0                              ;move X/Y to min endstops, so the head is out of the way
M84                         ;steppers off
G90                         ;absolute positioning
;CURA_PROFILE_STRING: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
