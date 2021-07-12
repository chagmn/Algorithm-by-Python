//
//  main.swift
//  신규 아이디 추천
//
//  Created by 창민 on 2021/07/12.
//

import Foundation

func solution(_ new_id:String) -> String {
    // 1,2
    var new_id = new_id.lowercased().filter{ $0.isLetter || $0.isNumber || $0 == "." || $0 == "_" || $0 == "-"}
    
    // 3
    while new_id.contains("..") {
        new_id  = new_id.replacingOccurrences(of: "..", with: ".")
    }
    
    // 4
    if new_id.hasPrefix(".") { new_id.removeFirst() }
    if new_id.hasSuffix(".") { new_id.removeLast() }

    // 5
    if new_id.count == 0 {
        new_id += "a"
    }
    
    // 6
    if new_id.count >= 16 {
        let removeRange = new_id.index(new_id.startIndex, offsetBy: 15)..<new_id.endIndex
        new_id.removeSubrange(removeRange)
        
        if new_id.hasSuffix(".") { new_id.removeLast() }
    }
    
    // 7
    if new_id.count <= 2 {
        let lastChr = String(new_id.popLast()!)
        while new_id.count < 3 {
            new_id += lastChr
        }
    }
    
    return new_id
}

var newid = "z-+.^."
print(solution(newid))
