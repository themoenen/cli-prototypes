import argparse

def acc(args):
    # Print welcome message
    print("HELLO WELCOME!")

def gt(args):
    # Switch to the "gt" context
    print("(gt)")

    if args.about:
        # Print information about the "gt" context
        print("This is the GT4SD module.")

def ds(args):
    # Switch to the "ds" context
    print("(ds)")

    if args.about:
        # Print information about the "ds" context
        print("This is the DS module.")

    # 'ds' subcommands
    if args.subcommand == "test1":
        # Print "test1" within the "ds" context
        print("(ds) test1")
    elif args.subcommand == "test2":
        # Print "test2" within the "ds" context
        print("(ds) test2")

def gs(args):
    # Switch to the "gs" context
    print("(gs)")

    if args.about:
        # Print information about the "gs" context
        print("This is the GS module.")

def dc(args):
    # Switch to the "dc" context
    print("(dc)")

    if args.about:
        # Print information about the "dc" context
        print("This is the DC module.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Acc CLI tool")
    subparsers = parser.add_subparsers(help="Commands", dest="command")

    # 'acc' command
    parser_acc = subparsers.add_parser("acc", help="Welcome screen")
    parser_acc.set_defaults(func=acc)
    subparsers_acc = parser_acc.add_subparsers(help="Commands", dest="subcommand")

    # 'acc gt' command
    parser_gt = subparsers_acc.add_parser("gt", help="Switch to GT4SD module")
    parser_gt.add_argument("--about", action="store_true", help="Print information about the GT4SD module")
    parser_gt.set_defaults(func=gt)

    # 'acc ds' command
    parser_ds = subparsers_acc.add_parser("ds", help="Switch to DS module")
    parser_ds.add_argument("--about", action="store_true", help="Print information about the DS module")
    subparsers_ds = parser_ds.add_subparsers(help="Commands", dest="subcommand")

    # 'acc ds test1' command
    parser_ds_test1 = subparsers_ds.add_parser("test1", help="Test command 1 within the DS module")
    parser_ds_test1.set_defaults(func=ds)

    # 'acc ds test2' command
    parser_ds_test2 = subparsers_ds.add_parser("test2", help="Test command 2 within the DS module")
    parser_ds_test2.set_defaults(func=ds)

    # 'acc gs' command
    parser_gs = subparsers_acc.add_parser("gs", help="Switch to GS module")
    parser_gs.add_argument("--about", action="store_true", help="Print information about the GS module")
    parser_gs.set_defaults(func=gs)

    # 'acc dc' command
    parser_dc = subparsers_acc.add_parser("dc", help="Switch to DC module")
    parser_dc.add_argument("--about", action="store_true", help="Print information about the DC module")
    parser_dc.set_defaults(func=dc)

    args = parser.parse_args()

    args.func(args)
