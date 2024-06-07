// SPDX-License-Identifier: UNLICENSED
pragma solidity ^0.8.13;
import "./BinaryRelated.sol";

contract Counter {
    uint256 public number;

    function setNumber(uint256 newNumber) public {
        number = newNumber;
    }

    function increment() public {
        number++;
    }

    function pow(uint256 fp, uint256 n) public pure returns (uint256) {
        return BinaryRelated.pow(fp, n);
    }
}
