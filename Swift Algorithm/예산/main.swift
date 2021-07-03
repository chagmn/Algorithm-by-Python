//
//  main.swift
//  예산
//
//  Created by 창민 on 2021/07/03.
//

import Foundation

func solution(_ d:[Int], _ budget:Int) -> Int {
    var sum = 0
    let sorted = d.sorted()
    var index = 0
    
    while sum < budget {
        sum += sorted[index]
        index += 1
        // 합계가 예산을 초과하는 경우 갯수 감소.
        if sum > budget {
            index -= 1
        }
        // 신청 금액을 다 지원하고도 예산이 남을 경우 종료
        if index+1 > sorted.count {
            break
        }
    }
  
    return index
}

var d = [1,3,2,5,4]
var budget = 9

print(solution(d, budget))
