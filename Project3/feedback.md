# Part 1, Triangle
## Exercise 1a (1/1p):
Good!

## Exercise 1b (1/1p):
You have named your function which finds a random starting point within a triangle `triangle()`. This is not a very descriptive name.

Otherwise good.

## Exercise 1c (1/1p):
Again, `corner()` is not a very intuitive name for the iteration function.

Looks good otherwise.

## Exercise 1d (1/1p):
Good!

## Exercise 1e (0.5/1p):
Okay, but you could do this much more efficiently without a for loop, by converting the `points` list to a numpy array and using the hint as given in the exercise:
~~~~python
points = np.array(points)

red = points[colors == 0]
green = points[colors == 1]
blue = points[colors == 2]
~~~~
This will effectively do the same as your loop, but it's much faster and much easier to read.

## Exercise 1f (0.5/1p):
This is not properly implemented. In your loop you do:
~~~~python
col += [(col[i] + colors[i+1])/2]
~~~~
here `colors[i+1]` is which corner was chosen for the current step (`j`). Instead of this, you should be adding an RGB-value (`r_j`), depending on which corner was chosen, as follows:
- if `j == 0`, the value should be `r_0 = (1, 0, 0)`
- if `j == 1`, the value should be `r_1 = (0, 1, 0)`
- if `j == 2`, the value should be `r_2 = (0, 0, 1)`

# Part 2, Generalization of the Chaos Game
## Exercise 2a (1/1p):
Good, but when you raise an error you should include a helpful message to explain what caused the error. For example:
~~~~python
if type(n) != int:
    raise TypeError("n must be an integer")
~~~~

## Exercise 2b (0.5/1p):
There are a couple problems here.

First of all, your `_generate_ngon()` method is not supposed to return the array of the corners. In fact, because you return before you set `self.corners = corners`, you never actually set `self.corners`, because the method stops running when it gets to the `return` statement.

The point of calling this method in the constructor, is that you shouldn't have to call it more than once. Once the points are generated, they don't change.

That's why we want to store the generated points as an attribute in the class (`self.corners`). Therefore, we should set `self.corners = np.array(corners)` in the `_generate_ngon()` method, and use `self.corners` in any other method which needs to use the points later.

## Exercise 2c (0.5/1p):
You don't need to use a loop here to generate an array of `self.n` length with random values. You can do this just by doing:
~~~~python
weight = np.random.random(self.n)
~~~~
which does exactly the same as all of this:
~~~~python
weight = [] 
for i in range(self.n):
    rand_weight = np.random.random()
    weight.append(rand_weight)
weight = np.array(weight)
~~~~

You are also calling `self._generate_ngon()` for each iteration of your loop, which is very unnecessary. Obviously, if you had stored the generated corners as `self.corners` properly, this wouldn't be an issue.

## Exercise 2d (0.5/1p):
Your method here is very confusing, and not particularly efficient.

To start off, you generate 1000 different starting points, which is not necessary at all. During the discard part of the iteration, you then select a random point from these points, and step towards one of the corners.

What you are _supposed_ to do here, is select _one_ starting point, start from this point, and run the iteration the given number of times, continuing from the newly generated point each time.

You have done this correctly for in `triangle.py`, so I'm not sure why you didn't get it right here.

## Exercise 2e (0.5/1p):
You are not supposed to call `iterate()` from within the `plot()` method. Otherwise OK, although you could have put a little bit more effort into making the plot pretty (for example making the points smaller).

## Exercise 2f (0.5/1p):
A couple things here. First of all, in your `plot()` method, you write:
~~~~python
colors = self.gradient_color()
~~~~
However, `self.gradient_color` is a property, so you should use this as if it was a regular attribute, like this:
~~~~python
colors = self.gradient_color
~~~~

Additionally, in the `gradient_color` property, you write:
~~~~python
color_list.append(self.X_indices(0))
~~~~
which should presumably be 
~~~~python
color_list.append(self.X_indices[0])
~~~~
since `self.X_indices` is a list, not a callable method.

## Exercise 2g (1/1p):
Your way of checking whether the filename ends with `.png` is a little clunky. An example of a better way is to use `outfile.split(".")`, and checking what the final element of the list it returns is.

However, your method works well enough the way it is.

## Exercise 2h (0.5/2p):
The idea behind your tests is good, but the implementation is clunky, and they don't work properly with pytest.

## Exercise 2i (1/1p):
Good.

# Part 3, Barnsley Ferns
## Exercise 3a (1/1p):
Good.

## Exercise 3b (1/1p):
Good.

## Exercise 3c (1/1p):
Good. A better way of calculating the cumulative probability would be to use `np.cumsum()`, as follows:
~~~~python
p_cumulative = np.cumsum(p)
~~~~
That way, you could change the probabilities in `p`, and the cumualtive probability would be properly updated.

## Exercise 3d (1/1p):
OK, but the exercise asks you to iterate 50000 times, and you only iterate 5000 times.

## Exercise 3e (1/1p):
OK, however your `.png` test is not perfect. For example I could save it as `barnsley_fern.png.pdf` without getting an error here.

# Part 4, Variations
## Exercise 4a (0.5/1p):
You're partway there, but not completely. There are some syntax errors, and you are not using `getattr()` correctly in the class.

## Exercise 4b (/1p):
Not done.

## Exercise 4c (/1p):
Not done.

## Exercise 4d (/2p):
Not done.

# Style and Git
## Style (1/3p):
Could be better. The style is mostly OK, but in some places it's a little clunky and difficult to read, and much of the code is more complicated than necessary. There is also very little documentation.

## Use of Git (0.5/1p):
OK. You have OK commit messages, although some of them are not very descriptive. You also haven't managed to `tag` your finished project correctly.

## Miscellaneous
This project could be better, but it's good enough for a pass. Please take a look at the feedback, and ask if anything is unclear.

## 18/30 points

If you have any questions about the exercises or the feedback you are welcome to send me an email: j.o.f.akerholm@fys.uio.no
