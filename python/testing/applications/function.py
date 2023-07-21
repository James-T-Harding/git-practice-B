def complicated(value):
    match value.split():
        case ["execute", *args]:
            return f"Execute with args: {args}"
        case ["count", *args]:
            return len(args)
        case ["length", argument]:
            return len(argument)
        case ["open", file]:
            return f"Open {file}"
        case ["close"]:
            return "Close the program"
