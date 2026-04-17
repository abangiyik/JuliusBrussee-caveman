from caveman import caveman


def test_hello_becomes_oog():
    assert caveman("Hello") == "OOG"


def test_i_am_becomes_me():
    assert caveman("I am happy") == "UGH! ME HAPPY"


def test_standalone_i_becomes_me():
    result = caveman("I need food")
    assert "ME" in result
    assert "FOOD" in result


def test_articles_removed():
    result = caveman("the big rock")
    assert "THE" not in result
    assert "BIG ROCK" in result


def test_th_becomes_d():
    result = caveman("this thing")
    assert "DIS" in result or "DING" in result


def test_very_becomes_much():
    result = caveman("very big")
    assert "MUCH" in result


def test_ing_stripped():
    result = caveman("I am running fast")
    assert "RUNN" in result
    assert "RUNNING" not in result


def test_ugh_prefix_added():
    result = caveman("big rock")
    assert result.startswith("UGH!")


def test_goodbye_becomes_grunt():
    assert caveman("goodbye") == "UGH! GRUNT"


if __name__ == "__main__":
    tests = [v for k, v in list(globals().items()) if k.startswith("test_")]
    passed = 0
    for t in tests:
        try:
            t()
            print(f"  PASS  {t.__name__}")
            passed += 1
        except AssertionError as e:
            print(f"  FAIL  {t.__name__}: {e}")
    print(f"\n{passed}/{len(tests)} passed")
