## YASS-WASM

This is [YASS](https://sourceforge.net/projects/sokobanyasc/) (Yet Another Sokoban Solver) 2.151 by Brian Damgaard, ported to WebAssembly.

* Added "-inline" option (YASS does not support stdin just yet)
* TODO: either add stdin support or dll calls support in wasm loader

### Usage

`YASS.exe -inline <space-separated level data>`

e.g.

`YASS.exe -inline "    #####       " "    #   #       " "  ###  $###     " "  #  $    #     " "### # ##  ######" "#   # ##$ #  ..#" "# $   $   $  ..#" "##### ### #  ..#" "    #  @  ######" "    #######     "`

Output: the last string either contains moves or "Level not solved" if no solution:

`rruuRRRRurDlllllddlllluuRRRRRRRRllllllllllulldRRRRRRRRRRRllluuulllulDDDuulldddrRRRRRRRdrUluRRlldlluuullluurDllddddrrrruuulLLulDDDuulldddrRRRRRRRdrUluRdllluulDuullldddrrRRRRurDldR`

(lowercase means "move", uppercase means "push")

Running in a browser (you can use a worker to run asynchronously):

```html
<!DOCTYPE html>
<html>
<head>
<script src="js/YASS_loader.js"></script>
<script>
let level = [
'    #####       ',
'    #   #       ',
'  ###  $###     ',
'  #  $    #     ',
'### # ##  ######',
'#   # ##$ #  ..#',
'# $   $   $  ..#',
'##### ### #  ..#',
'    #  @  ######',
'    #######     '
];
//rtl.showUncaughtExceptions=true;
rtl.argv = ["YASS", "-inline", ...level];
rtl.callback = result => {
  console.log(result);
}
rtl.run();
</script>
```

## Build

There are no WASM binary releases, you need LLVM 12.0.1 and FPC 3.2.2 to build cross-compiler from source.

* https://wiki.freepascal.org/WebAssembly
* https://wiki.freepascal.org/WebAssembly/Compiler

Prerequisites:

* https://github.com/llvm/llvm-project/releases/tag/llvmorg-12.0.1
* https://sourceforge.net/projects/freepascal/files/Win32/3.2.2/fpc-3.2.2.i386-win32.exe/download

```bat
git clone https://gitlab.com/freepascal.org/fpc/source.git fpc
cd fpc

:: build wasm compiler
set path=d:\lib\FPC\3.2.2\bin\i386-win32;%path%
set path=d:\lib\llvm\bin;%path%
make clean all OS_TARGET=wasi CPU_TARGET=wasm32 BINUTILSPREFIX= OPT="-O-" PP=fpc

:: install
mkdir d:\lib\fpcwasm
make crossinstall OS_TARGET=wasi CPU_TARGET=wasm32 INSTALL_PREFIX=d:\lib\fpcwasm PP=fpc

:: build YASS.wasm
set path=d:\lib\fpcwasm\bin\i386-win32;%path%
ppcrosswasm32.exe YASS.pas 
```

Then you need a bootstrap js code to load your .wasm, it's usually a Pascal program processed with [pas2js](https://wiki.freepascal.org/pas2js).

I've used [fpc_wasm example](https://github.com/mikewarot/fpc_wasm) and replaced `Wasm1.wasm` with `YASS.wasm`.

You also need to implement args_get and args_sizes_get to pass arguments to a program (see WASM_loader.js).

## References

* https://wiki.freepascal.org/WebAssembly
* https://github.com/mikewarot/fpc_wasm used as the main source
* https://www.freepascal.org/~michael/pas2js-demos/wasienv/terminal/ terminal demo
* https://github.com/fpc/pas2js/tree/main/demo/wasienv other examples
