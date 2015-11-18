
import sys, os

# complete hack, don't judge me please - just allow us to
# import directly from the example module in our tests
curr_dir = os.path.dirname(os.path.realpath(__file__))
mod_path = os.path.abspath(curr_dir + '/..')

sys.path.append(mod_path)
