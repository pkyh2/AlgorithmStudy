function solution(nums) {
  const uniqueItems = new Set(nums)
  const pickLen = nums.length / 2
  if (pickLen < uniqueItems.size) return pickLen
  else return uniqueItems.size
}

// N마리의 포켓몬 중 N/2마리를 가져가도 좋다.
// 최대한 많은 종류의 포켓몬을 포함해서 N/2를 선택하려고 한다.
// 



console.log(solution([3,1,2,3]))
console.log(solution([3,3,3,2,2,4]))
console.log(solution([3,3,3,2,2,2]))