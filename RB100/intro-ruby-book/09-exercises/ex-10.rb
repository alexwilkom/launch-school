# Can hash values be arrays? Can you have an array of hashes? (give examples)
# Yes, they can.
h = {
  array: [1, "error", true, [2, 3, 5, 7, 9]],
  array_of_hashes: [{a:1}, {b:2}, {c:3}]
}

p h