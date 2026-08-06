import sys

bitmap = """
....................................................................
    **************   *  *** **  *      ******************************
   ********************* ** ** *  * ****************************** *
  **      *****************       ******************************
           *************          **  * **** ** ************** *
            *********            *******   **************** * *
             ********           ***************************  *
    *        * **** ***         *************** ******  ** *
                ****  *         ***************   *** ***  *
                  ******         *************    **   **  *
                  ********        *************    *  ** ***
                    ********         ********          * *** ****
                    *********         ******  *        **** ** * **
                    *********         ****** * *           *** *   *
                      ******          ***** **             *****   *
                      *****            **** *            ********
                     *****             ****              *********
                     ****              **                 *******   *
                     ***                                       *    *
                     **     *                    *
...................................................................."""
# Take inpuut for the Bitmap message
print("Enter the Bitmap Message:")
message = input("> ")
#Exit the program if the message is empty
if message == "":
    sys.exit()

# Take Each line in the bitmap and print it with the message characters
for line in bitmap.splitlines():
    # For each character in the line, print the space if it is a space.
    for i, bit in enumerate(line):
        if bit == " ":
            print(" ", end="")
    # If it is not a space, print a character from the message.
    # The character printed is determined by taking the remainder of i divided by the length of the message.
        else:
            print(message[i % len(message)], end="")
    print()