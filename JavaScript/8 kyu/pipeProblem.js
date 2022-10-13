function pipeFix(arr) {
  let start = arr[0]
  let end = arr.slice(-1)
  let res = []
  for (let i = start; i <= end; i++) {
    res.push(i)
  }
  return res
}
