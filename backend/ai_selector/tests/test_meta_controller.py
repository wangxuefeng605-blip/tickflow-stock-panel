from core.meta.meta_controller import MetaController



def test_meta_controller():


    controller = MetaController()


    result = controller.process(

        {
            "momentum":0.5
        },

        0.4,

        0.6
    )


    assert result["evaluation"]["should_keep"] is True

    assert result["optimization"]["optimized"] is True

    assert result["state"]["cycles"] == 1