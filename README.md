# Chaotic Drawing using Trigonometric Functions.

Inspired by [this](http://www.artsnova.com/latoocarfian-chaotic-function-tutorial.html) article.

NOTE: You will need tkinter to be installed in your environment.

### How does this work?
We start with some small values of x,y then we use a formula to calculate new x,y values from the old ones. But that wouldn't be that interesting at all, so the idea is to plug in small and precise numbers (up to 17 decimal places) as constants to the equation. Those are only constant in one one drawing, as they are randomized in every drawing, you will most likely never encouter them again, which makes every drawing unique.

Formula:

    x = funcX1(y_old + a) + c*funcX2(x_old + a)
    y = funcY1(x_old + b) + d*funcY2(y_old + b)
where a,b,c,d are randomized constants.
and funcXX can be:
 * sin,
 * cos,
 * tan,
 * (feel free to try something else).


There are 1944 possible combinations of functions. (4! * 3^4)
Where each combination can drastically (or slightly) change the drawing. This means that there is <b>a lot</b> of exploring.


### How to use?
 
#### Exploring:

`python main.py`

You will be greeted by CLI input, you have to specify starting functions (space separated), eg:
`functions (x1, x2, y1, y2): cos sin sin tan`

hotkeys:
* f -> change functions (in prompt).
* s -> save this drawing.
* 'space' -> next drawing.
* q -> quit.
  
### Loading:

`python load.py`

This loads pickled drawing objects from `parameters/` folder.

Navigate through them with arrow keys (left, right).


## Sample Drawings:
![sin cos sin cos 0](/images/sin-cos-sin-cos0.png)