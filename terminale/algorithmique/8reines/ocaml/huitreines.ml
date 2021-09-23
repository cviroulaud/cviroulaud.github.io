
let huitreines =
  let placements = Array.make 8 1000 in
  let rec placer ligne =
    if ligne==8 then true
    else
      begin
      for col=0 to 7 do
        let possible = ref true in
        for k=0 to (ligne-1) do
          begin
          if (placements.(k)= col || 
            (placements.(k)+k) = (col+ligne) ||
          (placements.(k)-k) = (col-ligne)) then
            possible:= false;
          if !possible then
            (placements.(ligne)<-col;
            if placer (ligne+1) then true)
            end
            done;
        done;
        false
      end in
      placer 0;placements;;
let t = huitreines;;
