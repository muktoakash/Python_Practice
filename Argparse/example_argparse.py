import argparse
parser = argparse.ArgumentParser()
# parser.add_argument("echo", help="echo the string you use here")
# args = parser.parse_args()
# print(args.echo)

# argparse treats the options we give it as strings, unless we tell it otherwise.
# parser.add_argument("square", help="display a square of a given number", type=int)
# args = parser.parse_args()
# print(args.square**2)

# display something when --verbosity is specified and display nothing when not.
# parser = argparse.ArgumentParser()
# parser.add_argument("--verbosity", help="increase output verbosity")
# args = parser.parse_args()
# # if an optional argument isn’t used, args.verbosity is given None as a value
# # When using the --verbosity option, one must also specify some value, any value.
# if args.verbosity:
#     print("verbosity turned on")

# # display something when --verbosity is specified and display nothing when not.
# parser = argparse.ArgumentParser()
# parser.add_argument("-v", "--verbose", help="increase output verbosity", action="store_true")
# # The option is now more of a flag than something that requires a value.
# # if the option is specified, assign the value True to args.verbose. 
# # Not specifying it implies False.
# args = parser.parse_args()
# if args.verbosity:
#     print("verbosity turned on")

parser.add_argument("x", type=int, help="the base")
parser.add_argument("y", type=int, help="the exponent")
parser.add_argument("-vw", "--verbose", action="store_true",
                    help="increase output verbosity")
parser.add_argument("-v", "--verbosity", type=int,
                    help="increase output verbosity", choices=[0, 1, 2], default=0)
args = parser.parse_args()
answer = args.x**args.y
if args.verbose:
    print("{}^{} == ".format(args.x, args.y), end="")
else:
    pass
if args.verbosity == 2:
    print("Running '{}'".format(__file__))
elif args.verbosity == 1:
    print("{}^{} == ".format(args.x, args.y), end="")
else:
    print(answer)