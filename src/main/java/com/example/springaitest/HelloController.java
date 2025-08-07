package com.example.springaitest;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

/**
 * 简单的Hello World控制器
 * 
 * @author neilyou
 * @version 1.0
 */
@RestController
public class HelloController {

    /**
     * 返回Hello World消息
     * 
     * @return Hello World字符串
     */
    @GetMapping("/")
    public String hello() {
        return "Hello World! Spring Boot应用启动成功！";
    }
} 