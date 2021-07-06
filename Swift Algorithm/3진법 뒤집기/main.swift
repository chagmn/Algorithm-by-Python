//
//  main.swift
//  3진법 뒤집기
//
//  Created by 창민 on 2021/07/06.
//

import Foundation

func solution(_ n:Int) -> Int {
    let tenToThree = String(n, radix: 3)
    return Int(String(tenToThree.reversed()), radix: 3)!
}

var n = 45
print(solution(n))
