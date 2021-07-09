//
//  main.swift
//  실패율
//
//  Created by 창민 on 2021/07/08.
//

import Foundation

// n : 스테이지 수, stages : 사용자의 현재 스테이지, (n+1)은 마지막까지 클리어한 사용자
func solution(_ N:Int, _ stages:[Int]) -> [Int] {
    var fail = [Int:Double]()

    for i in 1...N {
        // 도달한 사람
        let people = stages.filter { $0 >= i }.count
        // 클리어한 사람
        let clear = stages.filter { $0 == i }.count
        
        fail.updateValue(Double(clear)/Double(people), forKey: i)
    }
    let sorted = fail.sorted(by: <).sorted(by: { $0.value > $1.value })

    let answer = sorted.map{ $0.key }
    return answer
}

var n = 5
var stages = [2,1,2,6,2,4,3,3]

print(solution(n, stages))
