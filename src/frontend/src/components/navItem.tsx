import { Link } from "react-router-dom";
import { cn } from "../lib/utils";
import React from "react";

interface NavLinkProps {
  name: string;
  url: string;
  icon?: React.ReactNode;
  isSeperated?: boolean;
}
const NavItem: React.FC<NavLinkProps> = ({
  name,
  url,
  icon,
  isSeperated,
}: NavLinkProps) => {
  return (
    <div
      className={cn(
        "flex flex-row items-center justify-start gap-2 py-2 hover:bg-indigo-50  text-gray-600 hover:font-bold hover:text-indigo-600 w-full",
        isSeperated ? "border-b-2 border-gray-200" : ""
      )}
    >
      {icon ? icon : null}
      <Link
        to={url}
        className="text-xl font-mediumbold py-2 block w-full text-{inherit}"
      >
        {name}
      </Link>
    </div>
  );
};
export default NavItem;
