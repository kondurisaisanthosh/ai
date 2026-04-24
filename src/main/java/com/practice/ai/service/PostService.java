package com.practice.ai.service;

import com.practice.ai.model.Post;
import org.springframework.stereotype.Service;
import org.springframework.web.client.RestTemplate;

@Service
public class PostService {

    private final RestTemplate restTemplate = new RestTemplate();

    private static final String BASE_URL =
            "https://jsonplaceholder.typicode.com/posts";

    public Post[] getAllPosts() {
        return restTemplate.getForObject(BASE_URL, Post[].class);
    }

    public Post getPostById(int id) {
        return restTemplate.getForObject(BASE_URL + "/" + id, Post.class);
    }
}