import { createApi, fetchBaseQuery } from '@reduxjs/toolkit/query/react';

export const reviewsApi = createApi({
    reducerPath: 'reviews',
    baseQuery: fetchBaseQuery({
        baseUrl: process.env.REACT_APP_API_HOST,
    }),
    tagTypes: ['reviews', 'comments'],
    endpoints: builder => ({
        getReview: builder.query({
            query: (review_id) => `/reviews/${review_id}`,
            providesTags: ['reviews'],
        }),
        getComments: builder.query({
            query: (review_id) => `/reviews/${review_id}/comments`,
            providesTags: ['comments'],
        }),
        postComment: builder.mutation({
            query: (params) => ({
                url: `/reviews/${params.id}/comments`,
                credentials: 'include',
                body: params.body,
                method: 'POST',
            }),
            invalidatesTags: ['comments'],

        }),
        deleteReview: builder.mutation({
            query: (review_id) => ({
                url: `/reviews/${review_id}`,
                credentials: 'include',
                method: 'DELETE',
            }),

        }),
    }),
});

export const {
    useGetReviewQuery,
    useDeleteReviewMutation,
    useGetCommentsQuery,
    usePostCommentMutation,
    } = reviewsApi;
