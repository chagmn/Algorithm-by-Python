//
//  main.swift
//  내적
//
//  Created by 창민 on 2021/06/30.
//

import Foundation

func solution(_ a:[Int], _ b:[Int]) -> Int {
    var b = b
    return a.map{$0 * b.removeFirst()}.reduce(0,+)
}


let a = [1,2,3,4]
let b = [-3,-1,0,2]
print(solution(a,b))
