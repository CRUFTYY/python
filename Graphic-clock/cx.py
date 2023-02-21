import cx_Freeze

executables = [cx_Freeze.Executable("graphic_clock.py")]

cx_Freeze.setup(
    name="graphic_clock",
    options={"build_exe": {"packages":["tkinter"]}},
    executables = executables
    )
