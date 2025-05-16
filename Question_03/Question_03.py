import turtle

def cheker(num): #Erro Hadeling
    try:
        float_num = abs(float(num))
    except ValueError:
        ascii_value = [ord(char) for char in num]
        float_num = sum(ascii_value)
    return min(float_num, 359.0)

def draw_tree(branch_length, t, left_angle, right_angle, depth, reduction_factor):
    if depth == 0 or branch_length < 1:
        return
    # Draw the branch
    t.pensize(depth) # Set thickness based on depth
    t.color("brown")  # trunk and branches in brown
    t.forward(branch_length)
    
    # Draw left branch
    t.left(left_angle)
    draw_tree(branch_length * reduction_factor, t, left_angle, right_angle, depth - 1, reduction_factor)
    
    # Return to original position and heading
    t.right(left_angle + right_angle)
    
    # Draw right branch
    draw_tree(branch_length * reduction_factor, t, left_angle, right_angle, depth - 1, reduction_factor)
    
    # Return to previous position
    t.left(right_angle)
    t.backward(branch_length)

def main():
    # Get user inputs
    left_angle = cheker(input("Enter left branch angle in degrees: "))
    right_angle = cheker(input("Enter right branch angle in degrees: "))
    start_length = cheker(input("Enter starting branch length in pixels: "))
    depth = cheker(input("Enter recursion depth: "))
    reduction_factor = cheker(input("Enter branch length reduction factor (e.g., 0.7): "))

    # Set up the turtle
    screen = turtle.Screen()
    t = turtle.Turtle()
    t.speed("fastest")
    t.left(90)  # Point the turtle upwards
    t.up()
    t.backward(100)
    t.down()
    t.color("brown")
    
    # Draw the tree
    draw_tree(start_length, t, left_angle, right_angle, depth, reduction_factor)
    
    screen.exitonclick()

if __name__ == "__main__":
    main()
