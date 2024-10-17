outfile = '../YASS/levels.dat';

levels = [[
'----#####-------',
'----#   #-------',
'--###  $###-----',
'--#  $    #-----',
'### # ##  ######',
'#   # ##$ #  ..#',
'# $   $   $  ..#',
'##### ### #  ..#',
'----#  @  ######',
'----#######-----' 
],[
'-#####-######---',
'-#   #-#    #---',
'-# $ ### ## ####',
'-# # #   $  $@ #',
'-# ###  $  $ # #',
'## # #####  $  #',
'#  #  ###  #####',
'#           ...#',
'##  #####   ...#',
'-####---########' 
],[
'########--------',
'#.##   ########-',
'#.## $ $ $    #-',
'#.## $    # # ##',
'#.### ## ## #  #',
'#.###$## ## ## #',
'#.     # ## $  #',
'#. $@$    #   ##',
'#.####    #####-',
'###--######-----' 
],[
'################',
'#........#     #',
'##  ###### ##  #',
'-#  # @    ##$ #',
'-#  #$# #####  #',
'-#  # $ #   #$ #',
'-#$    $#$# #  #',
'-#   #      $  #',
'-#####  ###   ##',
'-----####-#####- '
],[
'#######--#######',
'#     ##-#     #',
'# ###  ### ### #',
'# #### .. $### #',
'# #### ## $    #',
'#    $ ## #### #',
'# ###$ .. #### #',
'# ### ###  ### #',
'#     #-##  @  #',
'#######--#######' 
],[
'##############--',
'#  ##        #--',
'# $##  ##$## ##-',
'#  ## $ $ ##  ##',
'##  ## ##@$  $ #',
'#  $   ## ###  #',
'#...   ##  ##  #',
'#...#  $   ##$ #',
'#...#  ##  ##  #',
'################' 
],[
'################',
'#.... #  ##    #',
'#     #$   $## #',
'# ##  $ @#     #',
'# ## ## ## #####',
'#$#  ## ## #####',
'# #   $ ##   $ #',
'# #  ##$$    # #',
'#....##   ##   #',
'################' 
],[
'-###############',
'-#   .  .  .   #',
'-#  ####### #  #',
'-## $  $  $.#$##',
'#####.. #   #  #',
'#   #..#### #$ #',
'# $  ..#  # #  #',
'# $$$$ @      ##',
'#     ###  #  #-',
'#######-#######-' 
],[
'-############---',
'##   #      ##--',
'#  $ #  $ $@ #--',
'#  # # $ $ $ #--',
'## ##### #####--',
'#  #  ##  ######',
'#         #  ..#',
'##  ####     ..#',
'-####--####  ..#',
'----------######' 
],[
'################',
'#   #   ##     #',
'# #$# $    $ # #',
'#   # # ###### #',
'##  @ #  $ $   #',
'## ####  # ###.#',
'#     $  # ###.#',
'#  #####$# ###.#',
'##         ....#',
'-###############' 
],[
'----------####--',
'#######---#  ###',
'#  #  #####    #',
'# $#. $   # .$@#',
'#  #.## $ ##.###',
'# $#.## $ ##.  #',
'#  $. #   $ .  #',
'#     ######  ##',
'###  ##----####-',
'--####----------' 
],[
'###############-',
'#   #......#  #-',
'# $ ####  ## $#-',
'### #  #   #  #-',
'#     @#   ## ##',
'# $$$$### ###  #',
'###            #',
'--# ## ##  #  ##',
'--#    ########-',
'--######--------' 
],[
'###############-',
'#..  #    ##  ##',
'#..     # $ $  #',
'#..  # #### #  #',
'######      # ##',
'---#@   ##### ##',
'--###$$ $  ##  #',
'--#   $ #      #',
'--#     #  #  ##',
'--#############-' 
],[
'---###-########-',
'--##.###  #   ##',
'-##...# $   $  #',
'##.. ## $ $ $ ##',
'#..     $ $ $ #-',
'#..  @  $ $ $ #-',
'##.. ## $ $ $ ##',
'-##...# $   $  #',
'--##.###  #   ##',
'---###-########-' 
],[
'################',
'#...#   ##     #',
'#...##$ ## ##$ #',
'#   ##  $  ##  #',
'# @ #  ## ###  #',
'##$##  ## ###$##',
'#  ##$ ## ###  #',
'#              #',
'##   #######  ##',
'-#####-----####-' 
],[
'-########-------',
'##..##  ##------',
'#.  .    #------',
'#.  .$   #######',
'##..### ###    #',
'#####   ###$ # #',
'# $   $    $ # #',
'# $ $ $####### #',
'#       @      #',
'################' 
],[
'####-----#######',
'#  ####### ....#',
'# $##   ## .##.#',
'#  ## $   $.##.#',
'##    $ $$ ....#',
'## #  $   ##$$ #',
'#  #####$$##  ##',
'#   $   @      #',
'##  #  ###     #',
'-###############' 
],[
'---#############',
'---#  ##.......#',
'#### @###$ #####',
'#   $$## $ #----',
'# #   ##   #####',
'# ## $###  #   #',
'# ##  ### ###$ #',
'#  $           #',
'####  ###  #  ##',
'---####-#######- '
],[
'######----######',
'#    #----#    #',
'# $  ######  . #',
'# $ ###  ### . #',
'# $ ###      . #',
'# $      ### . #',
'# $ ###  ### . #',
'# $  ######  . #',
'# @  #----#    #',
'######----######' 
],[
'###############-',
'#             #-',
'# $ $ $ $ $ $ #-',
'# # # # # # # ##',
'#....          #',
'#....  $  $  $ #',
'#....   $$ $$  #',
'#....  $  $  $ #',
'#....$@$  $  $ #',
'################' 
]]

print('writing', outfile)

f = open(outfile,'w')

for i,data in enumerate(levels):
    print(f'level {i+1}', file=f)
    print(file=f)
    for s in data:
        print(s, file=f)
    print(file=f)
