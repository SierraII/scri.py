scri.py - Image Triangle Generator Written In Python.
======

This script divides images up into squares specified by square_size and calculates the mean color of that square.  
Those squares are then divided up into two mirrored triangles that get given that mean color of the parent square.  
<br/>
The triangles (unless speficied by an ignore color), will get an outline color darker by n% as specified by the darken_factor. The triangles' three co-ordinates then get randomly by numbers between the co-ordinate itself and by the offset_factor.  

## Example Output

<p align="center">
    <img width = "300" src="https://github.com/SierraII/scri.py/blob/master/examples/Mark Zuckerberg.png?raw=true" alt=""/>
    <img width = "300" src="https://github.com/SierraII/scri.py/blob/master/examples/Elbert Einstein.png?raw=true" alt=""/>
    <img width = "300" src="https://github.com/SierraII/scri.py/blob/master/examples/Steve Jobs.png?raw=true" alt=""/>
    <img width = "300" src="https://github.com/SierraII/scri.py/blob/master/examples/Jimi Hendrix.png?raw=true" alt=""/>
    <img width = "300" src="https://github.com/SierraII/scri.py/blob/master/examples/Elon Musk.png?raw=true" alt=""/>
</p>
