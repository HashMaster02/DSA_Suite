from globals import BinaryTreeNode

tree = BinaryTreeNode(
    value=20,
    right= BinaryTreeNode(
            value= 50,
            right= BinaryTreeNode(
                value= 100,
                right= None,
                left= None,
            ),
            left= BinaryTreeNode(
                value= 30,
                right= BinaryTreeNode(
                    value= 45,
                    right= None,
                    left= None,
                ),
                left= BinaryTreeNode(
                    value= 29,
                    right= None,
                    left= None,
                )
            ),
        ),
    left= BinaryTreeNode(
        value= 10,
        right= BinaryTreeNode(
            value= 15,
            right= None,
            left= None,
        ),
        left= BinaryTreeNode(
            value= 5,
            right= BinaryTreeNode(
                value= 7,
                right= None,
                left= None,
            ),
            left= None,
        )
    )
)
