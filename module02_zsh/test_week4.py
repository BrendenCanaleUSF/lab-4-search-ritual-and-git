# test_always_passes:

# test_string_is_lowercase
assert 2 + 2 == 4
assert "ism3232" == "ism3232".lower()
assert "ism3232" == "ism3232".upper()  # should fail

# test_strong_is_lowercase
name = "ism3232"
assert name == "ism3232".lower()
# test_path_segments
path = "a/ism3232/b"
print(path)
parts = path.split("/")
print(parts)
assert "ism3232" in parts
