import files.package1.file1
import files.package1.file2

import files.package1 as pack1

print(pack1.file1.f11)
pack1.file2.func21()

print(pack1.my_module.get_sum(3, 5, 7))
print(pack1.dataframes_filter.div_line) # ImportError: attempted relative import beyond top-level package



