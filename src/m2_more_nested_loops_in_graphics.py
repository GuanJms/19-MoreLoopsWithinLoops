"""
This project demonstrates NESTED LOOPS (i.e., loops within loops)
in the context of TWO-DIMENSIONAL GRAPHICS.

Authors: David Mutchler, Vibha Alangar, Matt Boutell, Dave Fisher,
         Mark Hays, Amanda Stouder, Aaron Wilkin, their colleagues,
         and Shengjun Guan.
"""  # DONE: 1. PUT YOUR NAME IN THE ABOVE LINE.

import rosegraphics as rg


def main():
    """ Calls the other functions to test them. """
    run_test_draw_upside_down_wall()


def run_test_draw_upside_down_wall():
    """ Tests the    draw_upside_down_wall    function. """
    # Tests 1 and 2 are ALREADY DONE (here).
    window = rg.RoseWindow(550, 300, 'Upside-down wall, Tests 1 and 2')

    rectangle = rg.Rectangle(rg.Point(125, 230), rg.Point(155, 250))
    draw_upside_down_wall(rectangle, 8, window)

    rectangle = rg.Rectangle(rg.Point(375, 175), rg.Point(425, 225))
    draw_upside_down_wall(rectangle, 4, window)

    window.close_on_mouse_click()


def draw_upside_down_wall(rectangle, n, window):
    """
    See   MoreWalls.pdf   in this project for pictures that may
    help you better understand the following specification:

    Draws an "upside-down wall" on the given window, where:
      -- The BOTTOM of the wall is a single "brick"
            that is the given rg.Rectangle.
      -- There are n rows in the wall.
      -- Each row is a row of "bricks" that are the same size
            as the given rg.Rectangle.
      -- Each row has one more brick than the row below it.
      -- Each row is centered on the bottom row.

    Preconditions:
      :type rectangle: rg.Rectangle
      :type n: int
      :type window: rg.RoseWindow
    and n is nonnegative.
    """
    # -------------------------------------------------------------------------
    # TODO: 2. Implement and test this function.
    #     Some tests are already written for you (above).
    # -------------------------------------------------------------------------
    upper_point_x = rectangle._upper_left_corner.x - 0.5 * rectangle.get_width() * (n-1)
    upper_point_y = rectangle._upper_left_corner.y -   rectangle.get_height() * (n-1)
    lower_point_x = rectangle._lower_right_corner.x - 0.5 * rectangle.get_width() * (n-1)
    lower_point_y = rectangle._lower_right_corner.y -  rectangle.get_height() * (n-1)

    x1 = upper_point_x
    y1 = upper_point_y
    x2 = lower_point_x
    y2 =lower_point_y

    for i in range(n):
        for j in range(i):
            x1 = x1 + rectangle.get_width()*0.5
            x2 = x2 + rectangle.get_width()*0.5

        for k in range(n-i+1):
            rec = rg.Rectangle(rg.Point(x1, y1),rg.Point(x2, y2))
            rec.outline_thickness = rectangle.outline_thickness
            rec.attach_to(window)
            window.render()
            x1 = x1 + rectangle.get_width()


        x1 = upper_point_x
        x2 = lower_point_x
        y1 = y1 + rectangle.get_height()
        y2 = y2 + rectangle.get_height()




# -----------------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# -----------------------------------------------------------------------------
main()
