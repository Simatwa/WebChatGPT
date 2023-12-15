import json

request_payload = json.loads("""{
    "action": "next",
    "messages": [
        {
            "id": "aaa2921d-d8c9-4516-80bd-ed1ea6895b84",
            "author": {
                "role": "user"
            },
            "content": {
                "content_type": "text",
                "parts": [
                    "Is this correct for sure?"
                ]
            },
            "metadata": {}
        }
    ],
    "conversation_id": "ef19ca72-4a7c-464e-8b0e-db36a0dc3734",
    "parent_message_id": "5b45a98c-0871-48ed-895b-f36f188c3d50",
    "model": "text-davinci-002-render-sha",
    "timezone_offset_min": -180,
    "suggestions": [],
    "history_and_training_disabled": false,
    "arkose_token": null,
    "conversation_mode": {
        "kind": "primary_assistant"
    },
    "force_paragen": false,
    "force_rate_limit": false
}""")

request_payload_org_1 = {
    "action": "next",
    "messages": [
        {
            "id": "aaa262a0-d409-449b-8e03-1a80db1383c9",
            "author": {
                "role": "user"
            },
            "content": {
                "content_type": "text",
                "parts": [
                    "Write a script to automate sending daily email reports in Python, and walk me through how I would set it up."
                ]
            }
        }
    ],
    "parent_message_id": "aaa1847b-9122-4f0c-9cf9-1f0a529b3cb0",
    "model": "text-davinci-002-render-sha",
    "timezone_offset_min": -180,
    "suggestions": [
        "Write a script to automate sending daily email reports in Python, and walk me through how I would set it up.",
        "I have a photoshoot tomorrow. Can you recommend me some colors and outfit options that will look good on camera?",
        "Tell me a random fun fact about the Roman Empire",
        "Show me a code snippet of a website's sticky header in CSS and JavaScript."
    ],
    "history_and_training_disabled": False,
    "arkose_token": None,
    "conversation_mode": {
        "kind": "primary_assistant"
    },
    "force_paragen": False,
    "force_rate_limit": False
}

request_payload_org = json.loads(
    """{
    "action": "next",
    "messages": [
        {
            "id": "aaa262a0-d409-449b-8e03-1a80db1383c9",
            "author": {
                "role": "user"
            },
            "content": {
                "content_type": "text",
                "parts": [
                    "Write a script to automate sending daily email reports in Python, and walk me through how I would set it up."
                ]
            }
        }
    ],
    "parent_message_id": "aaa1847b-9122-4f0c-9cf9-1f0a529b3cb0",
    "model": "text-davinci-002-render-sha",
    "timezone_offset_min": -180,
    "suggestions": [
        "Write a script to automate sending daily email reports in Python, and walk me through how I would set it up.",
        "I have a photoshoot tomorrow. Can you recommend me some colors and outfit options that will look good on camera?",
        "Tell me a random fun fact about the Roman Empire",
        "Show me a code snippet of a website's sticky header in CSS and JavaScript."
    ],
    "history_and_training_disabled": false,
    "arkose_token": null,
    "conversation_mode": {
        "kind": "primary_assistant"
    },
    "force_paragen": false,
    "force_rate_limit": false
}"""
)

request_cookies = {
    "__cf_bm": "H9nkBbW9dHKsa8d.ZebZzh._.RoS35l_0mhP0IARPdc-1702460863-1-ARgM6ruYrZDvsljCGPoaQDvObZj4BTapKO/UK+ieLXYTKxuMVwxBc9ei5TNWEqTctgW0U36cidl+iGeyb541TbQ=",
    "__cflb": "0H28vVfF4aAyg2hkHFH9CkdHRXPsfCUf5xL4qmo4odP",
    "__Host-next-auth.csrf-token": "c448c91874738318baf63689c4b71a4f85d26161062961f435bf6a1ef226954c%7C2edc0167de8db6325fd154eee5c7c5b7e22a3aca59792ba817edd5db3d322a0e",
    "__Secure-next-auth.callback-url": "https%3A%2F%2Fchat.openai.com",
    "__Secure-next-auth.session-token": "eyJhbGciOiJkaXIiLCJlbmMiOiJBMjU2R0NNIn0..YO0hJx2WzaTybzNY.FtpZkFuZTWPwnr1YO2M3e676fnooOlvBg5sWrUw6VKjST5tCJrpcmGwKASZqSY3wN62F37Sv5talllYeKPrLT2vMO3szw1egCvxjr62eqRzBtPmsiTyoICvrEidB0fbVpRZC9lHKbLeKgK-1JfYx1s0HFRZpw9OEMarOAyzMXiYYbag4dMaBanx6MLkkXrq7c-jUGdoYS6ixV9q9IYiPF5dr8epm2XPUYmsEC6Fmd1VGksiy705xyYwv3hj2HkJ9fYADm0niDk4e3b01vW_AVaFVR2vqagGuFQvBBnp__QAWR6xp6eHWMybU0-AAkIqQ_5BZd3P9oB25EZdSWzdeA6s-X9QCLR3YsOYQThGVnIq8tk-L1E1pyBa9DdF_GGswPNReS_q508dV4u0S-io5BqPVva35O-41heaYdnJQZa-gXLz-AqEvNXua-xnRfI1idC3-RtXjUPxnH2mPhw1LORddMdfM4auT7pbRCeobiRTY5TbTdBfjZgTYZDHCvzahGXSUu8SLK81IedsPNbY0FDNRT5lX9xU5kDav8c-sCFFx6RzNx0Wo0bfm1OQCEb7XqpeGW_LwbkYNLIFPquRplDWs_dI-pVnHN3X5cBnzn4aH3EyQF5Ge2BzyGqEp7oT_VKTZZbaXDjD8SGPwoJqr193tktadFLwuEc4Ir9SKayeLv_lNIM2bewAlRIRHZO67daPpt5obl-pz8rf1peNKaq3qgSoJyuXmndiPmheINaKVywSyQE6aCd7Y5EzfLtbUID7Job8QYENvot7DNAzvgZ3NI9f-d3UGH2baG06ylQQvIJbkX_TMetupyTAZrqO7BHnM6DZBaDPoH4y1RzCGrLugiOkngeYNp8m6pSM99jM3bmLpaZqxGD4YExM99eAOHgnx9S_iUWy3OO7ZxYJnpFOZSEXcG1ZXzChVg-J5ItBlxHPBH-2SjT84oFeU4Fv1shIV4A8lZftsKnEhFFFjMatPcDkORizx3rReLc1rRPhCabNp2000VNtubZ808cxn9xIhPKojrEvptGPJUjASC7CTP97kvFAH-YqToKD_dNlGEZSLzAnqgiqfXVOowozL82VweK1K3HwE2ZmhYPnnFloG0Asq7IjNKpeUxPh6cQ_Ft4aj7Wt5AO1oonYXISTdfXEi8ESCLCMe93-zCJSazWCIdwMfmfyjSgIRHcewKZ__bb5H-16zpm4_5nPMCx3YAgSZCq_-56mxKkp4sZ0r7_oEuSlpcxzPNRwF5W7WulwgvOI8gFYZPB9WbANtL4LOPjVARxNKYqipTVOJIZVAzPmaui_KTfsaJxtOYtDceJckdNR9w6Q8y_EvrOFBjuaHQcuaqP8sr8D6F-7QpnpQ1WGvxZlGpgFXjJzjshZQjl-bfexbifyI6QMrxhXdo7R9-RRdFBtqGKl6lDyaFXtsg9ufXIDSztc-glEp0BN6oJrG_yDMc-58IGw32VWAyUoJyYftkr9Wpetzj5hIwugxz4VcQIjLp7BSPuF_agoWBpvksJLmB0yuegxF7Cg-n6lHxVpxRhEYm7aS3kwVcla5cG6-E0eotUgW4Hy-aN3T39aw-WiorwtnBadowLgTBnzEDttnkO-6HxRedEi67sP354btqIDl4cnAr_qHSYRzO4wJIp9h_48JKtWtLEcs8Sohu3CbIxWDUD7PeLMyIjpoUmesXzmzrZfbMgGKM5NuDbLAe-iV9PAu7yt1rxxb4Ar7_YwPF74fYG9pOkb-lMgcyrTjvoDR4SbtyowqfsNr_ng65rvb7G7q1hDhh3c_WDj_-LcJGHsvHHY6FZ-snnwRWx4IB7Wv53GSCaYlMfUEsRhcioGbhCN11GV4RFohUEKz0Vb1EzK9iWPj8fRDYSYNOqwPD9iN9tsBJLOjy8_Va-fN7MEFjsCHRiah1CzqVjyLeSUYB8aj3s_y3To6scigkSshmCH3XW3PgeUenLs5HQ-lYXYJGsAJUAZ9BxNWFcYDvo3nJ3VTosdshwl5GK2Rr6A1N1h0stYPTJzOFr2AaY4-FysPM5-C2CGlDNG8blQWtLXcapYNBE5vWNzeU-ZzgNlGz6_elrcuSxvzZN2zOYA_atLSuHVcKFr5ibQNOGIccyaR3q1ec0o-zOQ2nYSPauIxSamdLDPOABmUe0f0e4QZBt_4UXTKhnbL4UTMBE3MzirOUaHydcgIgEM-0hMRcHb5yppz7mm-6Y5AobLKXw6rexMgy66FW4IvfcGrwOhoiBJF0QnXLqwEhpc_K--6SwZgDEiJuOIEZqwWHw4eSG3IJ3ZgfVuhmpzQWvvcwomPv4924KIp-LkogUdMKuVut6mPJtd5tNmapgy-1zRKDQAAO97QZFsuDK0m85bA1rOBOxz5gFaSmMd_2K_ulq0rQoChU451Puh_UmnvmKS1xvz_3f1EJwe4OrwOnxFvjzRN9T7PcKBEn6q-mepas0Q50TX_DWdQLoc4te-Tnx5rqMpeAlyVfsqSKp2o6-rnoY_LLNTUzrW0O9QU197dVIuNJX_NEb_vY0hhgvv9cmRSQzfUYwLVOqld-Px_Y2F-XTvGB3WqUj7MCN3r0OTG9MCq4fXMfLdBdzvulr-9k6ADzlRMOEWX9YxtxD5i62OD7yasfGNK1vCVJkzeHYz0yQhW5tWz0HZs7ayFFqfPfpZWnuAgpDmHKCaBuSynnJLMxct945tdtzz7q2L2G2b7JMfZHr4-Sn6kNWvPWtIECPW1SFMf5ZB2VXda6P30RPeMqZKafwIjri0NYRolW5h3nUPKcWunOBLiJBkiYGhMunpgUcN1-dSK6WCbK0qKjbMkcBCdAA.HKprGAfFnYiTlyh2uGi97g",
    "_cfuvid": "bxAWbJkwsNAk_Z1.tAc8Skxx7lm0Mq.XSHWQ2P1Mda0-1702460863889-0-604800000",
    "_dd_s": "rum=0&expire=1702461829475",
    "ajs_anonymous_id": "a0b59320-c342-4c9c-bb24-a99471552968",
    "ajs_user_id": "user-IUW2uKHQ6bwv4bdiI8IYtjqA",
    "cf_clearance": "1uGUVqave.DM7cSPP68eDuEIPyRq4myRL9Fmj8Ds.38-1702460867-0-1-ca1a82ea.5b1bdeef.739a9bce-0.2.1702460867",
    "intercom-device-id-dgkjq2bp": "38fd45fe-eb38-40b5-919e-b3974b213252",
    "intercom-session-dgkjq2bp": "ZkNYQmwzM000dGdaK1RRaERRSFhYSEdTSSt2dHpIYWJuMnlEc29qUTdaak1QSDJNeWI0VGRSMTVxSytxcmZvOC0tQXM3ZGNJWmpSTWxuM2FyNFgxbERzQT09--6cdc6de1601f203f8d1ab982fadf9685a606fec4",
}

request_headers = {
    "Accept": "text/event-stream",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "en-US",
    "Alt-Used": "chat.openai.com",
    "Authorization": "Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Ik1UaEVOVUpHTkVNMVFURTRNMEZCTWpkQ05UZzVNRFUxUlRVd1FVSkRNRU13UmtGRVFrRXpSZyJ9.eyJodHRwczovL2FwaS5vcGVuYWkuY29tL3Byb2ZpbGUiOnsiZW1haWwiOiJzbWFydHdhY2FsZWJAZ21haWwuY29tIiwiZW1haWxfdmVyaWZpZWQiOnRydWV9LCJodHRwczovL2FwaS5vcGVuYWkuY29tL2F1dGgiOnsicG9pZCI6Im9yZy1xZEd0UUM5ZXlsRkt6TTNLRzdlVERoRjAiLCJ1c2VyX2lkIjoidXNlci1JVVcydUtIUTZid3Y0YmRpSThJWXRqcUEifSwiaXNzIjoiaHR0cHM6Ly9hdXRoMC5vcGVuYWkuY29tLyIsInN1YiI6Imdvb2dsZS1vYXV0aDJ8MTA4ODk5NzU5MTgyMzA1MTAzOTUxIiwiYXVkIjpbImh0dHBzOi8vYXBpLm9wZW5haS5jb20vdjEiLCJodHRwczovL29wZW5haS5vcGVuYWkuYXV0aDBhcHAuY29tL3VzZXJpbmZvIl0sImlhdCI6MTcwMjQ2MDg2MywiZXhwIjoxNzAzMzI0ODYzLCJhenAiOiJUZEpJY2JlMTZXb1RIdE45NW55eXdoNUU0eU9vNkl0RyIsInNjb3BlIjoib3BlbmlkIGVtYWlsIHByb2ZpbGUgbW9kZWwucmVhZCBtb2RlbC5yZXF1ZXN0IG9yZ2FuaXphdGlvbi5yZWFkIG9yZ2FuaXphdGlvbi53cml0ZSBvZmZsaW5lX2FjY2VzcyJ9.2Wo6QF3M86Bkx9gAiYaPUuGcHMFTj0Oi_Hj9LcNMbD_QFMM5f7NgU8FDYYWjkaHnOHr9POtArmKigUSiopL2_RyBQsGw2oyWVig5MHVSMot82mKkBK7STFmBmSVUZkkI_Fhv6hgJ6CEUC4sO5ZUTk630UuSGQr10EOSszBrVI0_uLyJPi4RG5Psv-24QyCJrIdA8kSfeEecnBPiTUBoQTyZh0swJuAnUe_JzzfTSsU-jSZYh87LUkH8w3XekAuMuMzF_xCw44H0E8uuSHQK8s7oWiMwaMlCQA4gHNUIWa3YvxyRB4txkzlO7a9fjg3NEG7UF7Gg1W5kWPnh8lvo1dA",
    "Connection": "keep-alive",
    # "Content-Length": "904",
    "Content-Type": "application/json",
    "Host": "chat.openai.com",
    "Origin": "https://chat.openai.com",
    "Referer": "https://chat.openai.com/",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:120.0) Gecko/20100101 Firefox/120.0",
}
